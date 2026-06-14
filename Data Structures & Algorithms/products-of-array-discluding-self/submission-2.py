class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res  = [0]*len(nums)
        pref = [0]*len(nums)
        suff = [0]*len(nums)
        pref[0]=suff[-1]=1
        n = len(nums)
        for i in range(1,n):
            pref[i] = pref[i-1]*nums[i-1]
        for i in range(n-2,-1,-1):
            suff[i] = suff[i+1]*nums[i+1]
        for i in range(n):
            res[i]=pref[i]*suff[i]
        return res