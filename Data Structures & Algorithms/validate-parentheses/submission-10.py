class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        hashMap={'}':'{',')':'(',']':'['}

        for char in s:
            if char not in hashMap:
                stack.append(char)
            else:
                if len(stack)>0:
                    if stack.pop()!=hashMap[char]:
                        return False
                else:
                    return False
        return True if len(stack)==0 else False