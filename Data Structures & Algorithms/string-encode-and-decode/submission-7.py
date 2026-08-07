class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded=""
        for val in strs:
            encoded+=f"{len(val)}#{val}"
        return encoded

    def decode(self, s: str) -> List[str]:
        print(f"String: {s}")
        length=""
        res=[]
        val=0
        while(True):
            if not s:
                break
            while s[val] != '#' and s[val].isdigit():
                length+=s[val]
                val+=1
                print(f"val loop {val}")
            leng=int(length)
            print(leng)
            print(s[val+1:val+leng+1])
            print(val)
            res.append(s[val+1:val+leng+1])
            val=val+leng+1
            print(val)
            leng=0
            length=""
            if val > len(s)-1:
                break
        return res