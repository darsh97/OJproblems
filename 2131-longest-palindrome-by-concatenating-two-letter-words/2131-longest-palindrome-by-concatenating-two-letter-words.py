class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        cnt = Counter(words)
        total = 0

        for k, v in cnt.items():

            if k[0] != k[1]:
                r = k[::-1]
                if cnt[r] and v:
                    m = min(v, cnt[r])
                    total += m * 4
                    cnt[r] = 0

            else:
                total += (v - (v & 1)) * 2

        return total + (2 * any(e[0] == e[1] and v & 1 for e, v in cnt.items()))