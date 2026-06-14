class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        #case only one element
        if len(nums)==1:
            return nums[0]
        #case already sorted list
        if nums[r]>nums[0]:
            return nums[0]
        while(l<=r):
            mid=l+(r-l)//2
            if mid>0 and nums[mid-1]>nums[mid]:
                return nums[mid]
            if mid<len(nums) and nums[mid+1]<nums[mid]:
                return nums[mid+1]

            if nums[mid]>=nums[0]:
                #we have to look for smaller values in the right half
                l=mid+1
            else:
                r=mid-1