#dp[i][rgb]
N=int(input())
r,g,b=dict(),dict(),dict()
for i in range(N):
    r[i],g[i],b[i]=map(int,input().split())
dp=[[0]*3 for _ in range(N)]
dp[0][0]=r[0]
dp[0][1]=g[0]
dp[0][2]=b[0]
for i in range(1,N):
    dp[i][0]=min(dp[i-1][1],dp[i-1][2])+r[i]
    dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + g[i]
    dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + b[i]
print(min(dp[N-1]))