R,C,T=map(int,input().split())
l=[list(map(int,input().split())) for _ in range(R)]
di=[0,0,1,-1]
dj=[1,-1,0,0]
for i in range(R):
    if l[i][0]==-1:
        clean=i
        break

def diffuse(i,j,l,m):
    if l[i][j]==0:
        return
    if l[i][j]==-1:
        m[i][j]=-1
        return
    z=[]
    for k in range(4):
        ni,nj=i+di[k],j+dj[k]
        if 0<=ni<R and 0<=nj<C and not l[ni][nj]==-1:
            z.append((ni,nj))
    m[i][j]+=(l[i][j]-len(z)*(l[i][j]//5))
    for ni,nj in z:
        m[ni][nj]+=(l[i][j]//5)
    return
def whole_diffuse(l):
    m=[[0]*C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            diffuse(i,j,l,m)
    return m
def wind(l):
    #above
    #1)take last elements of second row and put it end of first row
    l[0].insert(C,l[1].pop(C-1))
    #2)pull up whole last column
    for i in range(1,clean): l[i].insert(C-1,l[i+1].pop(C-1))
    #3)pull down whole first column
    for i in range(clean,0,-1):l[i].insert(0,l[i-1].pop(0))

    #below
    # 1)
    l[R-1].insert(C, l[R-2].pop(C - 1))
    # 2)pull down whole last column
    for i in range(R-2, clean+1,-1): l[i].insert(C - 1, l[i - 1].pop(C - 1))
    # 3)pull up whole first column
    for i in range(clean+1,R-1): l[i].insert(0, l[i + 1].pop(0))
    l[clean][0],l[clean+1][0]=-1,-1
    l[clean][1], l[clean + 1][1] =0,0
    return

for _ in range(T):
    l=whole_diffuse(l)
    wind(l)
print(sum(map(sum,l))+2)