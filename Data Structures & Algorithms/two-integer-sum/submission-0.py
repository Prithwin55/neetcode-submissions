class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        ptr1=0
        ptr2=len(nums)-1
        for i in range(len(nums)):
            if nums[ptr1]+nums[ptr2]==target:
                return [ptr1,ptr2]
            elif nums[ptr1]+nums[ptr2]>target:
                ptr2-=1
            else:
                ptr1+=1