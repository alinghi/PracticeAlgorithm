N,M=map(int,input().split())
l=[list(input()) for _ in range(N)]
coin=[]
for i in range(N):
    for j in range(M):
        if l[i][j]=='o':
            coin.append((i,j))
            l[i][j]='.'
coin1=(coin[0][0],coin[0][1])
coin2=(coin[1][0],coin[1][1])
di=(0,0,1,-1)
dj=(1,-1,0,0)
def move(dir,i,j):
    ni,nj=i+di[dir],j+dj[dir]
    if not (0<=ni<N and 0<=nj<M):
        return -1
    if l[ni][nj]=='#':
        return i,j
    else:
        return ni,nj
def BFS():
    frontier = [(coin1,coin2)]
    level = {(coin1, coin2):0}
    i=1
    while frontier:
        next=[]
        for c1,c2 in frontier:
            for v in range(4):
                ret1=move(v,c1[0],c1[1])
                ret2 = move(v, c2[0], c2[1])
                if ret1==-1 and ret2==-1:
                    continue
                elif ret1==-1 or ret2==-1:
                    return i
                else:
                    level[(ret1,ret2)]=i
                    next.append((ret1,ret2))
        i=i+1
        if i>10:
            return -1
        frontier=next

print(BFS())