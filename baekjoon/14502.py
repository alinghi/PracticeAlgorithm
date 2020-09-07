import itertools
N,M=map(int,input().split())
l=[list(map(int,input().split())) for _ in range(N)]
candidates=[]
virus=[]
for i in range(N):
    for j in range(M):
        if l[i][j]==0:
            candidates.append((i,j))
        elif l[i][j]==2:
            virus.append((i,j))
def BFS(l,candidate):
    m=[row[:] for row in l]
    for i,j in candidate:
        m[i][j]=1
    i=1
    frontier=virus[:]
    while frontier:
        next=[]
        for u0,u1 in frontier:
            for v0,v1 in [(u0-1,u1),(u0+1,u1),(u0,u1-1),(u0,u1+1)]:
                if 0<=v0<N and 0<=v1<M and m[v0][v1]==0:
                    m[v0][v1]=2
                    next.append((v0,v1))
        frontier=next
        i=i+1
    ret=0
    for i in range(N):
        for j in range(M):
            if m[i][j]==0:
                ret+=1
    return ret

ans=0
for candidate in itertools.combinations(candidates,3):ans=max(BFS(l,candidate),ans)
print(ans)