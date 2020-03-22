# Knuth–Morris–Pratt (KMP) Algorithm


def compute_lps(s: str):
    # return lps table aka Longest proper Prefix which is also Suffix
    # O(|s|) because k can only be increased by 1 for each loop, and is decrease by at least 1 for each while loop

    lps, k = [0], 0
    for i in range(1, len(s)):
        while k > 0 and s[i] != s[k]:
            k = lps[k - 1]
        if s[i] == s[k]:
            k += 1
        lps.append(k)
    return lps
