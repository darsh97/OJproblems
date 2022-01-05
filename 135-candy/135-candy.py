class Solution:
    def candy(self, arr):
        n = len(arr)
        inc = [1] * n
        dec = [1] * n

        for i in range(1, n):
            if arr[i] > arr[i - 1]:
                inc[i] = 1 + inc[i - 1]

        for j in range(n - 2, -1, -1):
            if arr[j] > arr[j + 1]:
                dec[j] = 1 + dec[j + 1]

        return sum(max(a, b) for a, b in zip(inc, dec))