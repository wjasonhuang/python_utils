class Solution(object):
    def longestDupSubstring(self, s):
        #construct suffix arrary O(nlog(n)), optimal O(n)
        #sa: suffix array of s, sa[i]: start position of i-th suffix
        #rk[i]: ranking of suffix s[i:]
        #last element of s has to be the smallest otherwise add '@'

        n = len(s)
        sa = sorted([i for i in range(n)], key=lambda i: s[i])
        rk = [0] * n
        for i in range(1, n): rk[sa[i]] = rk[sa[i-1]] + (s[sa[i]] != s[sa[i-1]])

        k = 1
        new_sa = [0] * n
        new_rk = [0] * n
        while k < n:
            #update sa using counting sort O(n)
            count = [0] * (rk[sa[n-1]]+1)            
            for i in rk: count[i] += 1
            for i in range(rk[sa[n-1]]): count[i+1] += count[i]
            for i in reversed(range(n)):
                start = (sa[i] + n - k) % n
                count[rk[start]] -= 1
                new_sa[count[rk[start]]] = start
            sa, new_sa = new_sa, sa
            
            #update rk
            if k * 2 >= n: break
            for i in range(1, n):
                new_rk[sa[i]] = new_rk[sa[i-1]] + (rk[sa[i]] != rk[sa[i-1]] or rk[(sa[i]+k)%n] != rk[(sa[i-1]+k)%n])
            rk, new_rk = new_rk, rk

            k *= 2

        #construct longest common prefix array using Kasai algorithm O(n)
        #lcp[i]: longet common prefix between sa[i] and sa[i+1]
        #idx[i]: index in suffix array of suffix s[i:]
        lcp = [0] * n
        idx = [0] * n
        for i in range(n): idx[sa[i]] = i
        k = 0
        for i in range(n):
            k = max(k-1, 0)
            if idx[i] == n - 1:
                k = 0
                continue
            j = sa[idx[i]+1]
            while i+k<n and j+k<n and s[i+k]==s[j+k]: k+=1
            lcp[idx[i]] = k
        
        length = max(lcp)
        pos = sa[lcp.index(length)]
        return s[pos:pos+length]
