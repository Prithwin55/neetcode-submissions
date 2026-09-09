class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap={}
        frequency=[[] for _ in range(len(nums)+1)] #len(nums)+1 because 0-6 occurences not 0-5
        for val in nums:
            hashMap[val]=hashMap.get(val,0) + 1

        for key,val in hashMap.items():
            frequency[val].append(key)

        res=[]
        for i in range(len(nums),-1,-1):
            for val in frequency[i]:
                res.append(val)
                if len(res)== k:
                    return res
