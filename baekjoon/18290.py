N,M,K=map(int,input().split())
l=[list(map(int,input().split())) for _ in range(N)]
check=[[False]*M for _ in range(N)]
ans=-9e9
def encoder(i,j):
    return i*M+j
def decoder(i):
    return i//M, i%M
def checker(i):
    row,col=decoder(i)
    if row-1>=0 and check[row-1][col]:
        return False
    if col-1>=0 and check[row][col-1]:
        return False
    return True
def DFS(current, cnt,last):
    if cnt==K:
        global ans
        ans=max(ans,current)
        return
    for i in range(last+1,N*M):
        if checker(i):
            check[i//M][i%M]=True
            DFS(current+l[i//M][i%M],cnt+1,i)
            check[i//M][i%M]=False
    return

DFS(0,0,-1)
print(ans)