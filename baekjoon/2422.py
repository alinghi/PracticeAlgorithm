N,M=map(int,input().split())
l=[list(map(int,input().split())) for _ in range(M)]
graph=[[False]*N for _ in range(N)]
for n in l:
    graph[n[0]-1][n[1]-1]=True
    graph[n[1]-1][n[0]-1] =True
cnt=0
for i in range(N):
    for j in range(i+1,N):
        for k in range(j+1,N):
            if graph[i][j] or graph[j][k] or graph[k][i]: continue
            cnt+=1
print(cnt)