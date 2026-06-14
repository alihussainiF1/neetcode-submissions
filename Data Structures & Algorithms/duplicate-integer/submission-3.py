class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dct = {}
        for i in nums:
            if i not in dct:
                dct[i]=1
            else: 
                dct[i]+=1
        for i in dct.values():
            if i>1:
                return True
        return False       
        