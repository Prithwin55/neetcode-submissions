class Solution:
    def isPalindrome(self, s: str) -> bool:
        l=0
        r=len(s)-1
        while l<r:
            if not self.isalphanumeric(s[l]):
                l+=1
                continue
            print(r)
            if not self.isalphanumeric(s[r]):
                r-=1
                continue
            if s[l].lower()==s[r].lower():
                l+=1
                r-=1
            else:
                return False
        return True

            

    def isalphanumeric(self,c):
        if ord('a')<=ord(c)<=ord('z') or ord('A')<=ord(c)<=ord('Z') or ord('0')<=ord(c)<=ord('9'):
            return True
        else:
            return False
