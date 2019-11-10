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


# producer-consumer using queue
from threading import Thread, Lock
from queue import Queue

class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        
        def crawler(lock):
            while True:
                startUrl = q.get()
                if startUrl == None: break
                startHost = startUrl.split('/')[2]
                urlList = htmlParser.getUrls(startUrl)
                with lock:
                    for url in urlList:
                        if url in visited or url.split('/')[2] != startHost: continue
                        visited.add(url)
                        q.put(url)
                q.task_done()
        
        n = 10
        threads, visited = [], set([startUrl])
        lock, q = Lock(), Queue()
        q.put(startUrl)
        
        for _ in range(n):
            t = Thread(target=crawler, args=(lock,))
            t.start()
            threads.append(t)
        q.join()
        for _ in range(n): q.put(None)
        for t in threads: t.join()
        return list(visited)
