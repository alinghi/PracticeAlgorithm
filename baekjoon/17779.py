N=int(input())
l=[list(map(int,input().split())) for _ in range(N)]
def gen(N):
    for y in range(0, N - 2):
        for x in range(1,N-1):
            for d1 in range(1,x+1):
                for d2 in range(1,N-x):
                    if y+d1+d2<N:
                        yield(y,x,d1,d2)
def painter(m,si,sj,li,lj,paint):
    for i in range(si,li+1):
        for j in range(sj,lj+1):
            m[i][j]=paint
di=[0,0,1,-1]
dj=[1,-1,0,0]
def DFS(m,i,j):
    if m[i][j]==5:
        return
    m[i][j]=5
    for k in range(4):
        ni,nj=i+di[k],j+dj[k]
        DFS(m,ni,nj)

def area(candidate):
    row,col,d1,d2=candidate
    #print(candidate)
    m=[[1]*N for _ in range(N)]
    painter(m,0,col+1,row+d2,N-1,2)
    painter(m, row+d1, 0, N-1, col-d1+d2-1, 3)
    painter(m, row + d2+1, col-d1+d2, N - 1, N-1, 4)
    for i in range(d2):
        for j in range(0,d1+1):
            m[row+j+i][col-j+i]=5
        for j in range(0,d1):
            m[row + j + i+1][col - j + i] = 5
    for j in range(0,d1+1):
        m[row+d2+j][col+d2-j]=5
    #print(m)
    return m
def calc(m):
    cnt=[0]*5
    for i in range(N):
        for j in range(N):
            cnt[m[i][j]-1]+=l[i][j]
    #print(cnt)
    #print(max(cnt)-min(cnt))
    return max(cnt)-min(cnt)
ans=9e9
for candidate in gen(N):
    #print("==")
    m=area(candidate)
    ans=min(calc(m),ans)
print(ans)