class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        ret = 0
        for n in nums:
            if n-1 in numSet:
                continue
            else:
                l=0
                while l+n in numSet:
                    l+=1
                ret = max(l,ret)
        return ret 
