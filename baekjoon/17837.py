N,K=map(int,input().split())
l=[list(map(int,input().split())) for _ in range(N)]
direction_changer=[-1,1,3,0,2]
di,dj=(-1,0,1,0),(0,1,0,-1)
horses=dict()
Map={(i,j):[] for i in range(N) for j in range(N)}
for i in range(K):
    row,col,dir=map(int,input().split())
    horses[i]=(row-1,col-1,direction_changer[dir])
    Map[(row-1,col-1)].append(i)

def movement(z):
    i,j,dir=horses[z]
    ni,nj=i+di[dir],j+dj[dir]
    if ni<0 or ni>=N or nj<0 or nj>=N or l[ni][nj]==2:
        ci,cj=i-di[dir],j-dj[dir]
        if ci < 0 or ci >= N or cj < 0 or cj >= N or l[ci][cj] == 2:
            horses[z]=(i,j,(dir+2)%4)
        else:
            horses[z] = (ci, cj, (dir + 2) % 4)
            if l[ci][cj]==0:
                for z1 in Map[(i,j)][Map[(i,j)].index(z):]:
                    horses[z1]=(ci,cj,horses[z1][2])
                Map[(ci,cj)].extend(Map[(i,j)][Map[(i,j)].index(z):])
                Map[(i,j)]=Map[(i, j)][:Map[(i, j)].index(z)]
            else:
                for z1 in Map[(i,j)][Map[(i,j)].index(z):]:
                    horses[z1]=(ci,cj,horses[z1][2])
                Map[(ci, cj)].extend(Map[(i, j)][Map[(i, j)].index(z):][::-1])
                Map[(i, j)] = Map[(i, j)][:Map[(i, j)].index(z)]
            if len(Map[(ci,cj)])>=4:
                return True
    elif l[ni][nj]==1:
        horses[z] = (ni, nj, dir)
        for z1 in Map[(i, j)][Map[(i, j)].index(z):]:
            horses[z1] = (ni, nj, horses[z1][2])
        Map[(ni, nj)].extend(Map[(i, j)][Map[(i, j)].index(z):][::-1])
        Map[(i, j)] = Map[(i, j)][:Map[(i, j)].index(z)]
        if len(Map[(ni,nj)])>=4:
            return True
    elif l[ni][nj]==0:
        horses[z] = (ni, nj, dir)
        for z1 in Map[(i, j)][Map[(i, j)].index(z):]:
            horses[z1] = (ni, nj, horses[z1][2])
        Map[(ni, nj)].extend(Map[(i, j)][Map[(i, j)].index(z):])
        Map[(i, j)] = Map[(i, j)][:Map[(i, j)].index(z)]
        if len(Map[(ni,nj)])>=4:
            return True
    return False
def display():
    print("--------")
    for i in range(N):
        for j in range(N):
            print(Map[(i,j)],end=" ")
        print()

def solution():
    turn=1
    while turn<1000:
        for z in range(K):
            ans=movement(z)
            if ans:
                return turn
        turn+=1
    return -1
print(solution())