n,k=map(int,input().split())
coins=[int(input()) for _ in range(n)]
coins=list(set(coins))
coins=sorted(coins)
dp=[99999999]*(k+1)
dp[0]=0
for coin in coins:
    for i in range(1,k+1):
        if i-coin>=0:
            dp[i]=min(dp[i-coin]+1,dp[i])
if dp[-1]==99999999:
    print(-1)
else:
    print(dp[-1])