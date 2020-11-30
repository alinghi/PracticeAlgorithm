N,M=map(int,input().split())
l1=[list(map(int,input().split())) for _ in range(N)]
l2=[[-1]*M for _ in range(N)]
l2[N-1][M-1]=1
dr=(0,0,1,-1)
dc=(1,-1,0,0)
def DFS(r,c):
    if l2[r][c]>=0:
        return l2[r][c]
    l2[r][c] = 0
    for dir in range(4):
        nr,nc=r+dr[dir],c+dc[dir]
        if 0<=nr<N and 0<=nc<M and l1[r][c]>l1[nr][nc]:
            l2[r][c]+=DFS(nr,nc)
    return l2[r][c]

DFS(0,0)
print(l2[0][0])