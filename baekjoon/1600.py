K=int(input())
W,H=map(int,input().split())
l=[list(map(int,input().split())) for _ in range(H)]
level = {(0, 0, K): 0}
for i in range(H):
    for j in range(W):
        if l[i][j]==1:
            for k in range(K+1):
                level[(i,j,k)]=-1
k1=[    [2,1],[2,-1],[1,2],[1,-2],[-2,1],[-2,-1],[-1,2],[-1,-2]]
k2=[    [1,0],[-1,0],[0,1],[0,-1]]
goal=(H-1,W-1)
def BFS():
    i = 1
    frontier = [(0, 0, K)]
    if (0,0)==goal:
        return 0
    while frontier:
        next = []
        for u in frontier:
            if u[2] > 0:
                for k in k1:
                    v = (u[0] + k[0], u[1] + k[1])
                    z = (u[0] + k[0], u[1] + k[1], u[2]-1)
                    if v==goal:
                        return i
                    if z not in level and  0<=z[0]<H and 0<=z[1]<W:
                        level[z]=i
                        next.append(z)
            for k in k2:
                v = (u[0] + k[0], u[1] + k[1])
                z = (u[0] + k[0], u[1] + k[1], u[2])
                if v == goal:
                    return i
                if z not in level and 0<=z[0]<H and 0<=z[1]<W:
                    level[z]=i
                    next.append(z)
        frontier = next
        i = i + 1
ans=BFS()
if ans==None:
    print(-1)
else:
    print(ans)