n,k=map(int,input().split())
l=[int(input()) for _ in range(n)]
l=sorted(l)
dp=[0]*(k+3+l[-1])
dp[0]=1
for coin in l:
    for i in range(0,k+1):
        if i-coin>=0:
            dp[i]+=dp[i-coin]
print(dp[k])