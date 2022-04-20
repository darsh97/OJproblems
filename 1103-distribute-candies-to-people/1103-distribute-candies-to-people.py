class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        k = 0

        for j in count(1):
            n = j * (j + 1) // 2
            if n >= candies:
                k = j
                break

        lst = [0] * num_people

        for i in range(1, k + 1):
            lst[i % num_people - 1] += min(i, candies)
            candies -= i
        return lst
