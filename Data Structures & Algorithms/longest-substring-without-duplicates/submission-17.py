class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest=0
        l=0
        r=0
        seen=set()
        while r<len(s):
            if s[r] not in seen:
                seen.add(s[r])
                longest=max(longest,len(seen))
                r+=1
            else:
                if s[l] in seen:
                    seen.remove(s[l])
                l+=1

        return longest