class Solution:
    def isValid(self, s: str) -> bool:

        look_up ={'}':'{',']':'[',')':'('}
        k = []
        for c in s : 
            if c not in look_up:
                k.append(c)
            else:
                if not k or k.pop() != look_up[c]:
                    return False
        return len(k) == 0
