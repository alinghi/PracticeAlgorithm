N=int(input())
l=[[False]*100 for _ in range(100)]
for _ in range(N):
    a,b=map(int,input().split())
    for i in range(a,min(a+10,100)):
        for j in range(b,min(b+10,100)):
            l[i][j]=True
cnt=0
for row in l:
    cnt+=sum(row)
print(cnt)