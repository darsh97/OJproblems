
class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:

        pos = {}

        for i, e in enumerate(nums):
            pos[e] = i

        for a, b in operations:
            nums[pos[a]] = b
            pos[b] = pos[a]
            del pos[a]

        return nums