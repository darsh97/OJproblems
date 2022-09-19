from string import ascii_lowercase as alphabets


d = dict(zip(alphabets, alphabets[1:]))


class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        prev = s[0]
        mx = cnt = 1
        for c in s[1:]:
            if d.get(prev, '') != c:
                cnt = 1
            else:
                cnt += 1

            prev = c
            mx = max(mx, cnt)

        return mx
    