class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack=[]
        reformip=[[p,s] for p,s in zip(position,speed)]

        reformip=sorted(reformip)[::-1] #sorted based on position in decending order of position

        for p,s in reformip:
            distance=(target-p)/s
            stack.append(distance)
            if len(stack)>=2 and stack[-1]<=stack[-2]:
                stack.pop()
        return len(stack)
