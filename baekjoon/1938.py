N=int(input())
l=[list(input()) for _ in range(N)]
B,E=[],[]
for i in range(N):
    for j in range(N):
        if l[i][j]=="B":
            B.append((i,j))
            l[i][j]=0
        elif l[i][j]=="E":
            E.append((i,j))
            l[i][j] = 0
for i in range(N):
    for j in range(N):
        l[i][j]=int(l[i][j])
#center_row,center_col,orientation(#0 vertical 1 horizontal)
B=(B[1][0],B[1][1],1) if B[0][0]==B[1][0] else (B[1][0], B[1][1], 0)
E=(E[1][0],E[1][1],1) if E[0][0]==E[1][0] else (E[1][0], E[1][1], 0)

check=[[[(-2,0)],[(-1,1),(0,1),(1,1)],[(2,0)],[(-1,-1),(0,-1),(1,-1)]],
        [[(-1,-1),(-1,0),(-1,1)],[(0,2)],[(1,-1),(1,0),(1,1)],[(0,-2)]]
       ]
rotates=[(1,-1),(1,0),(1,1),(-1,-1),(-1,0),(-1,1),(0,1),(0,-1)]

#v 0 up 1 right 2 down 3 left
dr=(-1,0,1,0)
dc=(0,1,0,-1)
def BFS():
    level = {B: 0}
    parent={B:None}
    i = 1
    frontier = [B]
    while frontier:
        next=[]
        for u in frontier:
            for v in range(4):
                deter=True
                for w in check[u[2]][v]:
                    if not (0<=u[0]+w[0]<N and 0<=u[1]+w[1]<N and l[u[0]+w[0]][u[1]+w[1]]==0):
                        deter=False
                        break
                if deter:
                    temp=(dr[v]+u[0],dc[v]+u[1],u[2])
                    if temp==E:
                        return i
                    if temp not in level:
                        level[temp]=i
                        parent[temp]=u
                        next.append(temp)
            deter=True
            for rotate in rotates:
                if not (0<=u[0]+rotate[0]<N and 0<=u[1]+rotate[1]<N and l[u[0]+rotate[0]][u[1]+rotate[1]]==0):
                    deter=False
                    break
            if deter:
                temp=(u[0],u[1],1-u[2])
                if temp==E:
                    return i
                if temp not in level:
                    level[temp] = i
                    parent[temp] = u
                    next.append(temp)
        frontier=next
        i=i+1
    return 0
print(BFS())