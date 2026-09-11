class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        s1count = [0] * 26
        s2count = [0] * 26

        for c in s1:
            s1count[ord(c) - ord('a')] += 1
        
        for r, c in enumerate(s2):
            if r - l + 1 > len(s1):
                s2count[ord(s2[l]) - ord('a')] -= 1
                l += 1

            s2count[ord(c) - ord('a')] += 1

            if s1count == s2count:
                return True

        return False