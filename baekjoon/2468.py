import sys
sys.setrecursionlimit(10**4)
N=int(input())
l=[list(map(int,input().split())) for _ in range(N)]
height_max=max(max(row) for row in l)
dr,dc=(0,0,1,-1),(1,-1,0,0)
def DFS(visited,r,c,rain):
    for dir in range(4):
        nr,nc=r+dr[dir],c+dc[dir]
        if 0<=nr<N and 0<=nc<N and not visited[nr][nc] and l[nr][nc]>rain:
            visited[nr][nc]=True
            DFS(visited,nr,nc,rain)

def DFS_visit(rain):
    #return number of conencted component
    visited=[[False]*N for _ in range(N)]
    cc=0
    for i in range(N):
        for j in range(N):
            if l[i][j]<=rain:
                visited[i][j]=True
            elif not visited[i][j]:
                visited[i][j]=True
                DFS(visited,i,j,rain)
                cc+=1
    return cc

ans=1
for rain in range(1,height_max):
    ans=max(ans,DFS_visit(rain))
print(ans)