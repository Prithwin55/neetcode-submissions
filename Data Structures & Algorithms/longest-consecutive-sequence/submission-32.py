class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ptr=0
        count=[1]*len(nums)
        nums=sorted(set(nums))

        for i in range(1,len(nums)):
            if abs(nums[i]-nums[i-1]) == 1:
                count[ptr]+=1
            else:
                ptr+=1
        return max(count,default=0)