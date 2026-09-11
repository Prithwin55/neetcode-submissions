class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l=0
        r=1
        maxp=0
        while r<len(prices):
            curr=prices[r]-prices[l]
            maxp=max(curr,maxp)
            if prices[r]<prices[l]:
                l=r
            r+=1
        return maxp