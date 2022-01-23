
class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        cnt = Counter(nums)
        res = []
        for e in nums:
            if cnt[e] > 1 or e + 1 in cnt or e - 1 in cnt:
                continue
            else:
                res.append(e)
        return res