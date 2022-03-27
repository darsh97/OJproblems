class Solution:
    def minDeletion(self, nums: List[int]) -> int:
        st = [nums[0], ]
        state = 0

        for i, e in enumerate(nums[1:], 1):
            m = len(st) - 1  # index of last element in stack
            if st[-1] == e:
                if state:
                    if not i % 2:
                        state ^= 1
                    else:
                        st.append(e)
                else:
                    if i % 2:
                        state ^= 1
                    else:
                        st.append(e)

            else:
                st.append(e)

        if len(st) % 2: st.pop()
        return len(nums) - len(st)
