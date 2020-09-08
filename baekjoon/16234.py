N,L,R=map(int,input().split())
l=[list(map(int,input().split())) for _ in range(N)]
di=[0,0,-1,1]
dj=[-1,1,0,0]

def BFS(indicator,i,j,cnt):
    frontier=[(i,j)]
    indicator[i][j]=cnt
    total=frontier
    level=cnt
    s=l[i][j]
    sc=1
    while frontier:
        next=[]
        for i,j in frontier:
            for v in range(4):
                ni,nj=i+di[v],j+dj[v]
                if 0<=ni<N and 0<=nj<N and indicator[ni][nj]==-1 and L<=abs(l[i][j]-l[ni][nj])<=R:
                    indicator[ni][nj]=level
                    next.append((ni,nj))
                    s+=l[ni][nj]
                    sc+=1
        frontier=next
        total.extend(next)
    s=s//sc
    for i,j in total:
        l[i][j]=s


def move():
    cnt=0
    ans=0
    while cnt!=N*N:
        indicator = [[-1] * N for _ in range(N)]
        cnt=0
        for i in range(N):
            for j in range(N):
                if indicator[i][j]==-1:
                    BFS(indicator,i,j,cnt)
                    cnt+=1
        ans+=1
    print(ans-1)
move()