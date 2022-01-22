class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        cnta, cntb = Counter(s), Counter(t)
        for k, v in cntb.items():
            if k not in cnta or cnta[k] != v:
                return k
            