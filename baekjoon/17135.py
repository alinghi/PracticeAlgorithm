import itertools
def archer_target(i,j,r,m):
    for k1 in range(1,r+1):
        for k2 in range(-k1+1,k1):
            #row,col adjustment
            ni,nj=i-abs(k1)+abs(k2),j+k2
            if 0<=ni<N and 0<=nj<M and m[ni][nj]==1:
                return ni,nj
    return (-1,-1)
N,M,D=map(int,input().split())
l=[list(map(int,input().split())) for _ in range(N)]
def kill(archers):
    score=0
    m=[row[:] for row in l]
    archer_list=[(N+1,k) for k in archers]
    for _ in range(N):
        archer_list=[(k[0]-1,k[1]) for k in archer_list]
        s=set()
        for archer in archer_list:
            ni,nj=archer_target(archer[0],archer[1],D,m)
            if ni==-1 and nj==-1:
                continue
            else:
               s.add((ni,nj))
        for ni,nj in s:
            m[ni][nj]=0
        score+=len(s)
    return score
ans=0
for archers in itertools.combinations([i for i in range(M)],3):
    ans=max(kill(archers),ans)
print(ans)