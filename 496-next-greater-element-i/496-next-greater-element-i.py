class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        st = []
        d = {}
        res = []

        for i, e in enumerate(nums2):
            if not st:
                st.append((e, i))
            else:
                while st and e > st[-1][0]:
                    v, j = st.pop()  # the previous smaller values
                    d[v] = e

                st.append((e, i))

        for i, e in enumerate(nums1):
            if e not in d:
                res.append(-1)
            else:
                res.append(d[e])

        return res
