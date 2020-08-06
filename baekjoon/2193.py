N=int(input())
l=[[0,0] for _ in range(91)]
l[1][1]=1
# nth 01
for i in range(2,N+1):
    l[i][0]=l[i-1][0]+l[i-1][1]
    l[i][1]=l[i-1][0]
print(l[N][0]+l[N][1])