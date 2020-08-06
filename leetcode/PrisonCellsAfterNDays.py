class Solution:
   
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        j=0
        d={}
        l=cells
        cycle=False
        cycleNumber=None
        while j<N and not cycle:
            l2=[0]*8
            for i in range(1,7):
                if l[i-1]==l[i+1]:
                    l2[i]=1
            l=l2[:]
            d[j+1]=l
            for z in range(1,j+1):
                if d[z]==l:
                    cycle=True
                    cycleNumber=(z,j+1)
                    break
            j=j+1
        if cycle:
            return d[(N-1)%(cycleNumber[1]-cycleNumber[0])+1]
        else:
            return l