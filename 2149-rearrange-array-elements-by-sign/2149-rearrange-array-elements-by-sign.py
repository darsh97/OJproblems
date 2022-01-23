class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        data = [[], []]

        for e in nums:
            data[e < 0].append(e)

        return list(chain.from_iterable(zip(*data)))

