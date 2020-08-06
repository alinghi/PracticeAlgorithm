class Solution:
    def arrangeCoins(self, n: int) -> int:
        i=0
        while True:
            if i*(i+1)//2<=n<(i+1)*(i+2)//2:
                break
            i=i+1
        return i
        