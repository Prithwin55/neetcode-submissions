class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group=[]
        mark=[0 for _ in range(len(strs))]
        count=0
        def isAnagram(s,t):
            s="".join(sorted(s))
            t="".join(sorted(t))
            if s==t :
                return True
            else:
                return False
        for i in range(len(strs)):
            if mark[i]==1:
                continue
            group.append([strs[i]])
            for j in range(i+1,len(strs)):
                if isAnagram(strs[i],strs[j]) and mark[j]!=1:
                    mark[j]=1
                    group[count].append(strs[j])
            count+=1
        return group