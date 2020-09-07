import itertools
N=int(input())
l=list(map(int,input().split()))
cand=[N-i-1 for i in range(1,N-1)]
cand=[list(range(i)) for i in cand]
def calc(i):
    m=l[:]
    score=0
    for j in i:
        score+=m[j]*m[j+2]
        m.pop(j+1)
    return score
ans=0
for i in itertools.product(*cand):
    ans=max(ans,calc(i))
print(ans)