# """
# This is HtmlParser's API interface.
# You should not implement it, or speculate about its implementation
# """
#class HtmlParser(object):
#    def getUrls(self, url):
#        """
#        :type url: str
#        :rtype List[str]
#        """

from threading import Thread, Lock

class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        
        def crawler(startUrl):
            nonlocal mutex
            
            startHost = startUrl.split('/')[2]
            urlList = htmlParser.getUrls(startUrl)
            with mutex:
                for url in urlList:
                    if url in visited or url.split('/')[2] != startHost: continue
                    visited.add(url)
                    q.append(url)
        
        q, visited = collections.deque([startUrl]), set([startUrl])
        n, mutex = 8, Lock()
        
        while q:
            threads = []
            while len(threads) < n and q:
                newUrl = q.popleft()
                newThread = Thread(target=crawler, args=[newUrl])
                threads.append(newThread)

            for t in threads: t.start()
            for t in threads: t.join()
        
        return list(visited)


from threading import Lock
from concurrent.futures import ThreadPoolExecutor

class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        
        def crawler(startUrl):
            nonlocal lock
            startHost = startUrl.split('/')[2]
            urlList = htmlParser.getUrls(startUrl)
            with lock:
                for url in urlList:
                    if url in visited or url.split('/')[2] != startHost: continue
                    visited.add(url)
                    newq.append(url)
        
        q, visited, lock = [startUrl], set([startUrl]), Lock() 
        while q:
            newq = []
            with ThreadPoolExecutor() as executor:
                executor.map(crawler, q)
            q = newq
        return list(visited)
