class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded=""
        for val in strs:
            encoded+=f"{len(val)}#{val}"
        return encoded

    def decode(self, s: str) -> List[str]:
        ptr=0
        res=[]
        while ptr < len(s):
            length=""
            while s[ptr] != '#':
                length+=s[ptr]
                ptr+=1
            length=int(length)
            res.append(s[ptr+1:ptr+length+1])
            ptr+=length+1
            length=""
        return res