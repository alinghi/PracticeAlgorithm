N,M=map(int,input().split())
l=[list(input()) for _ in range(N)]
row={"U":-1,"D":1,"L":0,"R":0}
col={"U":0,"D":0,"L":-1,"R":1}
supreme_visit=[[-1]*M for _ in range(N)]
def DFS(i,j):
    visited=[(i,j)]
    ret=-1
    while True:
        i,j=i+row[l[i][j]],j+col[l[i][j]]
        if not (0<=i<N and 0<=j<M):
            ret=1
            break
        if supreme_visit[i][j]!=-1:
            ret=supreme_visit[i][j]
            break
        visited.append((i,j))
        supreme_visit[i][j]=0
    if ret==1:
        for i,j in visited:
            supreme_visit[i][j]=1
    return ret

cnt=0
for i in range(N):
    for j in range(M):
        if supreme_visit[i][j]>=0:
            cnt+=supreme_visit[i][j]
        else:
            cnt+=DFS(i,j)
print(cnt)