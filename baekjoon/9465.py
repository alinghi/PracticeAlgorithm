def solution():
    n=int(input())
    p1=list(map(int,input().split()))
    p2=list(map(int,input().split()))
    p=[p1,p2]
    dp=[[0]*(n+1) for _ in range(2)]
    dp[0][1]=p[0][0]
    dp[1][1] = p[1][0]
    for i in range(2,n+1):
        dp[0][i]=max(dp[1][i-1],dp[1][i-2])+p[0][i-1]
        dp[1][i] = max(dp[0][i - 1], dp[0][i - 2]) + p[1][i-1]
    print(max(dp[0][n],dp[1][n]))

N=int(input())
for _ in range(N):
    solution()