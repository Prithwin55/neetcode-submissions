class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap=defaultdict(list)
        for val in strs:
            sortedS="".join(sorted(val))
            hashMap[sortedS].append(val)
        return list(hashMap.values())