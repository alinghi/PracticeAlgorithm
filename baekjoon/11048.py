N,M=map(int,input().split())
l=[list(map(int,input().split())) for _ in range(N)]
dp=[[0]*M for _ in range(N)]
for i in range(M):
    for j in range(N):
        a=dp[j][i-1]+l[j][i] if i-1>=0 else 0
        b=dp[j-1][i]+l[j][i] if j-1>=0 else 0
        dp[j][i]=max(a,b)
print(dp[-1][-1]+l[0][0])