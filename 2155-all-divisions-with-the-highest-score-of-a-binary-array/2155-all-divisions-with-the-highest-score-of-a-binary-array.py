class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        n = len(nums)
        zero_prefix = one_suffix = 0
        zero_prefix_array, one_suffix_array = [], []
        res = []

        for i in range(n):
            zero_prefix += not nums[i]
            one_suffix += nums[n - i - 1]

            zero_prefix_array.append(zero_prefix);
            one_suffix_array.append(one_suffix)

        one_suffix_array.reverse()

        for i in range(n - 1):
            res.append(zero_prefix_array[i] + one_suffix_array[i + 1])

        res = [one_suffix_array[0]] + res + [zero_prefix_array[-1]]
        mx = max(res)
        return [i for i, e in enumerate(res) if e == mx]
