import itertools
N,M=map(int,input().split())
l=[list(input()) for _ in range(N)]
di,dj=[-1,0,1,0],[0,1,0,-1]
for i in range(N):
    for j in range(M):
        if l[i][j]=="R":
            ri,rj=i,j
            l[i][j]='.'
        elif l[i][j]=="B":
            bi,bj=i,j
            l[i][j]='.'
        elif l[i][j]=="O":
            gi,gj=i,j
            l[i][j]='.'
def display(l,nri,nrj,nbi,nbj):
    for i in range(N):
        for j in range(M):
            if i==nri and j==nrj:
                print("R",end="")
            elif i==nbi and j==nbj:
                print("B",end="")
            elif i==gi and j==gj:
                print("O",end="")
            else:
                print(l[i][j],end="")
        print()

def simulator(moves):
    nri,nrj,nbi,nbj=ri,rj,bi,bj
    cnt=0
    for move in moves:
        cnt+=1
        ori,orj,obi,obj=nri,nrj,nbi,nbj
        nri,nrj=movement(move,nri,nrj)
        nbi, nbj = movement(move, nbi, nbj)
        if nri==nbi and nrj==nbj:
            if nri==gi and nrj==gj:
                return -1
            else:
                if move==0:
                    if ori<obi:
                        nbi+=1
                    else:
                        nri+=1
                elif move==1:
                    if orj<obj:
                        nrj-=1
                    else:
                        nbj-=1
                elif move==2:
                    if ori<obi:
                        nri-=1
                    else:
                        nbi-=1
                elif move==3:
                    if orj<obj:
                        nbj+=1
                    else:
                        nrj+=1
        if nbi==gi and nbj==gj:
            return -1
        if nri==gi and nrj==gj:
            return cnt
    return -1

def movement(direction,i,j):
    ni,nj=i,j
    while True:
        nni,nnj=ni+di[direction],nj+dj[direction]
        if l[nni][nnj]=="#":
            return ni,nj
        else:
            if gi==nni and gj==nnj:
                return gi,gj
            else:
                ni,nj=nni,nnj
    return None
def solver():
    for k in range(1,11):
        for moves in itertools.product([0,1,2,3],repeat=k):
            ret=simulator(moves)
            if ret==-1:
                continue
            else:
                return k
    return -1
print(solver())