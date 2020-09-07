import itertools
N,M,H=map(int,input().split())
l=[[False]*(N+1) for _ in range(H+1)]
cand=[]
for _ in range(M):
    a,b=map(int,input().split())
    l[a][b]=True
    cand.append((a,b))
def check():
    for i in range(1,N+1):
        where=i
        for h in range(1,H+1):
            if l[h][where]:
                where+=1
            elif l[h][where-1]:
                where-=1
        if where!=i: return False
    return True
candidates_list=[[False]+[True]*(N) for _ in range(H+1)]
candidates_list[0]=[False]*(N+1)
for i,j in cand:
    candidates_list[i][j] = False
    candidates_list[i][j-1]=False
    candidates_list[i][j + 1] = False
candidates=[]
for i in range(H+1):
    for j in range(N):
        if candidates_list[i][j]:
            candidates.append((i,j))
def solver():
    i=0
    while i<4:
        for candidate in itertools.combinations(candidates,i):
            for row,col in candidate:
                l[row][col]=True
            if check():
                return i
            for row,col in candidate:
                l[row][col]=False
        i=i+1
    return -1
print(solver())
