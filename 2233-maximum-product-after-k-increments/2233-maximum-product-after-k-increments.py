M = 10 ** 9 + 7

class Solution:
    def maximumProduct(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        res = 1
        for _ in range(k):
            top = heapq.heappop(nums)
            heapq.heappush(nums, top + 1)

        for e in nums:
            res = (res * e % M) % M
            
        return  res % M