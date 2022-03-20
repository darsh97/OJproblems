class Solution:
    def maximumSubsequenceCount(self, text: str, pattern: str) -> int:
        def subseq_cnt(text, pattern):
            sf, sfa = 0, []
            subseq_cnt = 0
            
            for e in reversed(text):
                sf += e == pattern[1]
                sfa.append(sf)

            sfa.reverse()

            for i, e in enumerate(text[:-1], 1):
                if e == pattern[0]:
                    subseq_cnt += sfa[i]

            return subseq_cnt

        return max(subseq_cnt(pattern[0] + text, pattern), subseq_cnt(pattern[-1] + text[::-1], pattern[::-1]))
