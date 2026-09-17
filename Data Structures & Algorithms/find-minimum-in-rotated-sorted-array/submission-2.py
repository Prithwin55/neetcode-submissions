class Solution:
    def findMin(self, nums: List[int]) -> int:
        l=0
        r=len(nums)-1
        minm=nums[l]
        while l<=r:
            if nums[l]<nums[r]:
                minm=min(minm,nums[l])
                break
            mid=(l+r)//2
            minm=min(nums[mid],minm)
            if nums[mid] >= nums[l]:
                l=mid+1
            else:
                r=mid-1
        return minm