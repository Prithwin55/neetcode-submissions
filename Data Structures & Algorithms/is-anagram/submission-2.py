class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sMap={}
        tMap={}

        for i in range(len(s)):
            sMap[s[i]]=sMap.get(s[i],0) + 1
            tMap[t[i]]=tMap.get(t[i],0) + 1
        print(sMap)
        print(tMap)
        for j in range(len(s)):
            if sMap.get(s[j],0) != tMap.get(s[j],0):
                return False
        else:
            return True