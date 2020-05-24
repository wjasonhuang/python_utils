# Knuth–Morris–Pratt (KMP) Algorithm
# Leetcode 28, 214


def compute_lps(s: str):
    # return lps table aka Longest proper Prefix which is also Suffix
    # O(|s|) because k can only be increased by 1 for each loop, and is decrease by at least 1 for each while loop

    lps, k = [0], 0
    for i in range(1, len(s)):
        while k > 0 and s[i] != s[k]: k = lps[k - 1]
        if s[i] == s[k]: k += 1
        lps.append(k)
    return lps


def KMP(s: str, p: str) -> int:
    # find the first occurrence of pattern p in string s

    if not p: return 0
    lps, n, kp, ks = [0], len(p), 0, 0

    for i in range(1, n):
        while kp > 0 and p[i] != p[kp]: kp = lps[kp - 1]
        if p[i] == p[kp]: kp += 1
        lps.append(kp)

    for i in range(len(s)):
        while ks > 0 and s[i] != p[ks]: ks = lps[ks - 1]
        if s[i] == p[ks]:
            ks += 1
            if ks == n:
                return i - n + 1

    return -1
