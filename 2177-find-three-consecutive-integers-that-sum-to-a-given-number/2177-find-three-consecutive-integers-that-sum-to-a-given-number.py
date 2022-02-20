class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        if num % 3:
            return []

        mid = num // 3
        a, b, c = (mid - 1), mid, (mid + 1)

        return [a, b, c] 