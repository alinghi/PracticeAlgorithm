class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n=0
        for digit in digits:
            n=n*10+digit
        n=n+1
        n=str(n)
        return list(n)