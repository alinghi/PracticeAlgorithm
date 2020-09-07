import itertools
N,M=map(int,input().split())
l=[list(map(int,input().split())) for _ in range(N)]
house=[]
chicken=[]
chicken_map=[]

dr=(0,0,1,-1)
dc=(1,-1,0,0)
def BFS(i,j):
    time=1
    m=[[-1]*N for _ in range(N)]
    m[i][j]=0
    frontier=[(i,j)]
    while frontier:
        next=[]
        for row,col in frontier:
            for k in range(4):
                nr,nc=row+dr[k],col+dc[k]
                if 0<=nr<N and 0<=nc<N and m[nr][nc]==-1:
                    next.append((nr,nc))
                    m[nr][nc]=time
        time=time+1
        frontier=next
    return m


for i in range(N):
    for j in range(N):
        if l[i][j]==1:
            house.append((i,j))
            l[i][j]=0
        elif l[i][j]==2:
            chicken.append((i,j))
            chicken_map.append(BFS(i,j))
            l[i][j] = 0
ans=9e9
for candidates in itertools.combinations(chicken_map,M):
    total_dist=0
    for hous in house:
        local_dist=9e9
        for candidate in candidates:
            local_dist=min(candidate[hous[0]][hous[1]],local_dist)
        total_dist+=local_dist
        if total_dist>ans:
            break
    ans=min(ans,total_dist)
print(ans)