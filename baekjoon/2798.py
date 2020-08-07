import itertools
N,M=map(int,input().split())
l=list(map(int,input().split()))
ans=0
for i in itertools.combinations(range(N),3):
    ret=0
    for j in i:
        ret+=l[j]
    if ret<=M:
        ans=max(ans,ret)
print(ans)