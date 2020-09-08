import sys
sys.setrecursionlimit(10**4)
N,M=map(int,input().split())

l=[list(input()) for _ in range(N)]
for i in range(N):
    for j in range(M):
        l[i][j]=int(l[i][j])
di=[0,0,1,-1]
dj=[1,-1,0,0]
def DFS(i,j,cnt):
    l[i][j]=cnt
    for k in range(4):
        ni,nj=i+di[k],j+dj[k]
        if 0<=ni<N and 0<=nj<M and l[ni][nj]==0:
            DFS(ni,nj,cnt)
cnt=2
for i in range(N):
    for j in range(M):
        if l[i][j]==0:
            DFS(i,j,cnt)
            cnt+=1
counter={i:0 for i in range(0,cnt)}
for i in range(N):
    for j in range(M):
        counter[l[i][j]]+=1
for i in range(N):
    for j in range(M):
        ret=set()
        cnt=0
        if l[i][j]==1:
            for k in range(4):
                ni,nj=i+di[k],j+dj[k]
                if 0 <= ni < N and 0 <= nj < M and l[ni][nj]>1:
                    ret.add(l[ni][nj])
            for s in ret:
                cnt+=counter[s]
            cnt+=1
            print(cnt%10,end="")
        if l[i][j]>1:
            print(0,end="")
    print()
