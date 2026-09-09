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

            

    def isalphanumeric(self,char):
        if (ord(char) >= ord('a') and ord(char) <= ord('z')) or (ord(char) >= ord('A') and ord(char) < ord('Z'))or (ord(char) >= ord('0') and ord(char) <= ord('9')):
            return True
        else:
            return False
