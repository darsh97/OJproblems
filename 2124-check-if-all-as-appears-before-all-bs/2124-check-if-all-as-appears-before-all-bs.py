class Solution:
    def checkString(self, s: str) -> bool:
        a = b = None
        for i, e in enumerate(s):
            if b is not None and a is not None:
                if a > b: return False

            if e == 'a':
                a = i
            elif e == 'b':
                b = i
        
        if b is None: return True
    
        return a is None or b > a
