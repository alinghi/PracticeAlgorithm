import itertools
N,M=map(int,input().split())
l=[list(map(int,input().split())) for _ in range(N)]
cctv_position=[]
watch=[(1,0),(-1,0),(0,1),(0,-1)]
dr=(1,-1,0,0)
dc=(0,0,1,-1)
cctv_watch=[[(0,),(1,),(2,),(3,)],[(0,1),(2,3)],[(0,2),(0,3),(1,2),(1,3)],[(0,1,2),(0,1,3),(2,3,0),(2,3,1)],[(0,1,2,3)]]
cctv_candidates=[]
for i in range(N):
    for j in range(M):
        if 1<=l[i][j]<=5:
            cctv_position.append((i,j,l[i][j]-1))
            cctv_candidates.append(cctv_watch[l[i][j]-1])
            l[i][j]=0
def calc(cctv):
    m=[row[:] for row in l]
    frontier=[]
    for i in cctv:
        m[i[1][0]][i[1][1]]=1
        bfs(m,i[0],i[1])
    return sum(row.count(0) for row in m)
    # direction, original position
def bfs(m,direction,position):
    frontier=[]
    for dir in direction:
        frontier.append((dir,position[0],position[1]))
    while frontier:
        next=[]
        for d,i,j in frontier:
            ni,nj=i+dr[d],j+dc[d]
            if 0<=ni<N and 0<=nj<M and l[ni][nj]!=6:
                m[ni][nj]=1
                next.append((d,ni,nj))
        frontier=next
    return

ans=9e9
for cctv_candidate in itertools.product(*cctv_candidates):
    ans=min(ans,calc(list(zip(cctv_candidate,cctv_position))))
print(ans)