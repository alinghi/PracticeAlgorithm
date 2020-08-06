N,M=map(int,input().split())
l=[list(map(int,input().split())) for _ in range(N)]
n=int(input())
for _ in range(n):
    i,j,x,y=map(int,input().split())
    ans=0
    for row in range(i-1,x):
        for col in range(j-1,y):
            ans+=l[row][col]
    print(ans)
