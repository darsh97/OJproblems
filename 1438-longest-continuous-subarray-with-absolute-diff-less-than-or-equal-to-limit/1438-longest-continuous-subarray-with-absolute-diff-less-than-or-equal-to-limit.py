class MinMaxQueue():
    def __init__(self):
        self.Q = deque([])
        self._miQ = deque([])
        self._mxQ = deque([])

    def enque(self, value):
        if not self.Q:
            self.Q.append(value)
            self._miQ.append(value)
            self._mxQ.append(value)
        else:
            self.Q.append(value)

            while self._miQ and self._miQ[-1] > value:
                self._miQ.pop()

            self._miQ.append(value)

            while self._mxQ and self._mxQ[-1] < value:
                self._mxQ.pop()

            self._mxQ.append(value)

    def deque(self):
        if self.Q[0] == self._miQ[0]:
            self.Q.popleft()
            self._miQ.popleft()

        elif self.Q[0] == self._mxQ[0]:
            self.Q.popleft()
            self._mxQ.popleft()

        else:
            self.Q.popleft()

    @property
    def get_max(self):
        return self._mxQ[0]

    @property
    def get_min(self):
        return self._miQ[0]


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        nums = nums + [0]

        q = MinMaxQueue()
        res = 1

        for e in nums:
            if not q.Q:
                q.enque(e)
                
            else:
                while q.Q and ((q.get_max - q.get_min) > limit):
                    q.deque()
                    
                res = max(len(q.Q), res)
                
                q.enque(e)

        return res
