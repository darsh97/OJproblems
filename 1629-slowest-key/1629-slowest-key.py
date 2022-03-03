class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        mx, res = releaseTimes[0], keysPressed[0]
        
        for i, (a, b) in enumerate(zip(releaseTimes, releaseTimes[1:]), start = 1):
            d = b - a
            e = keysPressed[i]
            if d == mx:
                res = max(res, e)
            if d > mx:
                mx, res = d, e
        return res