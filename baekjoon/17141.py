import itertools
N,M=map(int,input().split())
l=[list(map(int,input().split())) for _ in range(N)]
candidates=[]
di=[0,0,-1,1]
dj=[1,-1,0,0]
def indicator(m):
    ret=1
    for i in range(N):
        for j in range(N):
            if m[i][j]==0:
                return 9e9
            if m[i][j]>ret:
                ret=m[i][j]
    return ret

def BFS(l, candidate):
    m=[row[:] for row in l]
    frontier=list(candidate)
    for i,j in frontier:
        m[i][j]=2
    level=3
    while frontier:
        next=[]
        for i,j in frontier:
            for k in range(4):
                ni,nj=i+di[k],j+dj[k]
                if 0<=ni<N and 0<=nj<N and m[ni][nj]==0:
                    m[ni][nj]=level
                    next.append((ni,nj))
        frontier=next
        level=level+1
    return indicator(m)

for i in range(N):
    for j in range(N):
        if l[i][j]==2:
            candidates.append((i,j))
            l[i][j]=0
ans=9e9
for candidate in itertools.combinations(candidates,M):
    ans=min(ans,BFS(l,candidate))
if ans==9e9:
    print(-1)
else:
    print(ans-2)
