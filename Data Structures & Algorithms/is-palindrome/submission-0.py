class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.replace(" ","")
        s=re.sub(r'[^a-zA-Z0-9\s]', '', s)
        s=s.lower()
        print(s)
        if s==s[::-1]:
            return True
        else:
            return False