import sys
from collections import deque
N,M,K=map(int,sys.stdin.readline().split())
dr=[-1,-1,-1,0,0,1,1,1]
dc=[-1,0,1,-1,1,-1,0,1]
m=[[5]*N for _ in range(N)]
a=[list(map(int,sys.stdin.readline().split())) for _ in range(N)]
n=[list(map(int,sys.stdin.readline().split())) for _ in range(M)]
l=[[0]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        l[i][j]=deque()
for x,y,z in n:
    l[x-1][y-1].append(z)
for i in range(N):
    for j in range(N):
        sorted(l[i][j])
#input done
ans=0
for age in range(K):
    for i in range(N):
        for j in range(N):
            # spring
            alive,dead=deque(),0
            while len(l[i][j])>0:
                x=l[i][j].popleft()
                if x<=m[i][j]:
                    m[i][j]=m[i][j]-x
                    alive.append(x+1)
                else:
                    dead=dead+(x//2)
            l[i][j]=alive
            # summer
            m[i][j]=m[i][j]+dead

    for i in range(N):
        for j in range(N):
        # fall
            for tree in l[i][j]:
                if tree%5==0:
                    for k in range(8):
                        if 0<=i+dr[k]<N and 0<=j+dc[k]<N:
                            l[i+dr[k]][j+dc[k]].appendleft(1)
    #winter
            m[i][j]=m[i][j]+a[i][j]
#count
for i in range(N):
    for j in range(N):
        ans=ans+len(l[i][j])
print(ans)