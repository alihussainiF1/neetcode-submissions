class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        dct = {} 

        for i in range(len(nums)):
            dct[nums[i]] = i 
        print(dct)

        for i in range(len(nums)):
            x = (target - nums[i])

            if x in dct:
                if i != dct[x]:
                    return [i,dct[x]]