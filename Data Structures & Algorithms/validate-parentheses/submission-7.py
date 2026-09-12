class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for bracket in s:
            if bracket=='(' or bracket=='{' or bracket=='[':
                stack.append(bracket)
            else:
                if len(stack)>0:
                    if bracket==')' and stack.pop()!='(':
                        return False
                    elif bracket=='}' and stack.pop()!='{':
                        return False
                    elif bracket==']' and stack.pop()!='[':
                        return False
                else:
                    return False
        if len(stack)==0:
            return True
        else:
            return False

            