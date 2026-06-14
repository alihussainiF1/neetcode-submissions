class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dct={}
        for i in nums:
            print(dct)
            if i not in dct:
                dct[i] = 1
            else:
                return True 
        print(dct)
        return False
