class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        cnt = Counter(nums)
        s = set(nums)
        res = []
        for e in nums:
            if cnt[e] > 1 or e + 1 in s or e - 1 in s:
                continue
            else:
                res.append(e)

        return res
