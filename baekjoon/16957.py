N,M=map(int,input().split())
l=[list(map(int,input().split())) for _ in range(N)]
d=[[0]*M for _ in range(N)]
dr=(0,0,1,-1,1,1,-1,-1)
dc=(1,-1,0,0,1,-1,1,-1)
for i in range(N):
    for j in range(M):
        MIN=(l[i][j],i,j)
        for k in range(8):
            ni,nj=i+dr[k],j+dc[k]
            if 0<=ni<N and 0<=nj<M and l[ni][nj]<MIN[0]:
                MIN=(l[ni][nj],ni,nj)
        d[i][j]=(MIN[1],MIN[2])
def findParent(i,j):
    if d[i][j]==(i,j):
        return (i,j)
    else:
        d[i][j]=findParent(d[i][j][0],d[i][j][1])
        return d[i][j]
p=[[0]*M for _ in range(N)]
for i in range(N):
    for j in range(M):
        z=findParent(i,j)
        p[z[0]][z[1]]+=1
for i in range(N):
    for j in range(M):
        print(p[i][j],end=" ")
    print()