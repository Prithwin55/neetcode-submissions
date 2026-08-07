class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        no_zeros=0
        total_product=1
        res=[0 for _ in range(len(nums))]
        for i in range(len(nums)):
            if nums[i] == 0:
                no_zeros+=1
                continue
            total_product*=nums[i]

        for i in range(len(nums)):
            if no_zeros >1:
                return [0]*len(nums)
            elif no_zeros == 1 and nums[i]==0:
                res=[0]*len(nums)
                res[i]=total_product
                return res
            else:
                res[i]=total_product // nums[i]
            

        return res