class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap=defaultdict(int)
        for val in nums:
            hashMap[val]+=1
        top_k=top_2_keys = sorted(hashMap, key=hashMap.get, reverse=True)[:k]
        return top_k