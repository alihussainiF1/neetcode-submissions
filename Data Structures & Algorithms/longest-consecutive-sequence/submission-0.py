class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet= set(nums)
        longest_length=0
        for n in nums:
            if n-1 not in numSet:
                length=0
                while n+length in numSet:
                    length+=1
                longest_length=max(longest_length,length)
        return longest_length