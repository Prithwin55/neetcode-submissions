class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest=0
        nset=set(nums)
        for num in nums:
            length=0
            if (num-1) not in nset:
                while num+length in nset:
                    length+=1
                longest=max(longest,length)
        return longest