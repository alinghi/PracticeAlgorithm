import sys
N,M=map(int,sys.stdin.readline().split())
l=[list(map(int,sys.stdin.readline().split())) for _ in range(N)]
match=[0,2,0,3,1]
dR=[0,-1,0,1]
dC=[-1,0,1,0]
x1,y1,z1=map(int,input().split())
x1,y1,z1=x1-1,y1-1,match[z1]
x2,y2,z2=map(int,input().split())
x2,y2,z2=x2-1,y2-1,match[z2]
visited=[[[False]*M for _ in range(N)] for _ in range(4)]
bfs=[]
bfs.append((x1,y1,z1,0))
visited[z1][x1][y1]=True
while True:
    r,c,dir,cnt=bfs.pop(0)
    if r==x2 and c==y2 and dir==z2:
        print(cnt)
        break
    for i in range(1,4):
        nr=r+dR[dir]*i
        nc = c + dC[dir] * i
        if nr<0 or nr>=N or nc<0 or nc>=M: break
        if visited[dir][nr][nc]:continue
        if l[nr][nc]==1: break
        bfs.append((nr,nc,dir,cnt+1))
        visited[dir][nr][nc]=True
    for i in (1,-1):
        ndir=(dir+i)%4
        if visited[ndir][r][c]:continue
        bfs.append((r,c,ndir,cnt+1))
        visited[ndir][r][c] = True