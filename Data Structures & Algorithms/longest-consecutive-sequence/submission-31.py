class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ptr=0
        count=[1]*len(nums)
        nums=sorted(set(nums))

        if len(nums)==1:
            return 1
        for i in range(1,len(nums)):
            diff=abs(nums[i]-nums[i-1])
            if diff == 1:
                count[ptr]+=1
            else:
                ptr+=1
        return max(count,default=0)