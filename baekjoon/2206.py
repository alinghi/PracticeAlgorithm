import collections
N,M=map(int,input().split())
level={}
l=[list(input()) for _ in range(N)]
q=collections.deque()
q.append((0,0,0))
dr=(0,0,1,-1)
dc=(1,-1,0,0)
level[(0,0,0)]=0
while q:
    row,col,wall=q.popleft()
    for dir in range(4):
        nrow,ncol=row+dr[dir],col+dc[dir]
        if 0<=nrow<N and 0<=ncol<M:
            if l[nrow][ncol]=='0' and (nrow,ncol,wall) not in level:
                level[(nrow,ncol,wall)]=level[(row,col,wall)]+1
                q.append((nrow,ncol,wall))
            if l[nrow][ncol]=='1' and wall==0 and (nrow,ncol,1) not in level:
                level[(nrow,ncol,1)]=level[(row,col,0)]+1
                q.append((nrow,ncol,1))

a=level.get((N-1,M-1,0))+1 if level.get((N-1,M-1,0))!=None else 9e9
b=level.get((N-1,M-1,1))+1 if level.get((N-1,M-1,1))!=None else 9e9
ans=min(a,b)
print(-1 if ans==9e9 else ans)