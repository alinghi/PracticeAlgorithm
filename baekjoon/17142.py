import itertools
N,M=map(int,input().split())
l=[list(map(int,input().split())) for _ in range(N)]
candidates=[]
di=[0,0,-1,1]
dj=[1,-1,0,0]
for i in range(N):
    for j in range(N):
        if l[i][j]==2:
            candidates.append((i,j))
ans=9e9
def BFS(l,candidate, candidates):
    m=[row[:] for row in l]
    level=3
    visit=dict()
    for i,j in candidates: visit[(i,j)]=False
    for i, j in candidate: visit[(i, j)] = True
    frontier=list(candidate)
    while frontier:
        next=[]
        for i,j in frontier:
            for k in range(4):
                ni,nj=i+di[k],j+dj[k]
                if 0<=ni<N and 0<=nj<N and m[ni][nj]==0:
                    m[ni][nj]=level
                    next.append((ni,nj))
                if 0 <= ni < N and 0 <= nj < N and m[ni][nj] == 2 and visit[(ni,nj)]==False:
                    visit[(ni,nj)]=True
                    next.append((ni,nj))
        frontier=next
        level=level+1
    ret=0
    for i in range(N):
        for j in range(N):
            if m[i][j]==0:
                return 9e9
            ret=max(ret,m[i][j])
    return ret-2
ans=9e9
for candidate in itertools.combinations(candidates,M):
    ans=min(ans,BFS(l,candidate,candidates))
ans=-1 if ans==9e9 else ans
print(ans)