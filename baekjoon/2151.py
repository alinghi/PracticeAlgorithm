N=int(input())
l=[list(input()) for _ in range(N)]
sharp=[]
for i in range(N):
    for j in range(N):
        if l[i][j]=="#":
            sharp.append((i,j))
dr,dc=(-1,0,1,0),(0,1,0,-1)
def display(x):
    z=[[0]*N for j in range(N)]
    for c in x:
        z[c[0]][c[1]]+=1
    print("----------------")
    for i in range(N):
        for j in range(N):
            if l[i][j]=="#":
                print("#",end=" ")
            elif z[i][j]==0:
                print("-",end=" ")
            else:
                print(z[i][j],end= " ")
        print()


def BFS(sharp):
    x1,x2=sharp[0]
    level={}
    frontier=[]
    parent={}
    ans=9e9
    for i in range(4):
        level[(x1,x2,i)]=0
        parent[(x1,x2,i)]=None
        frontier.append((x1,x2,i))
    while frontier:
        next=[]
        for u in frontier:
            nrow,ncol=u[0]+dr[u[2]],u[1]+dc[u[2]]
            if 0<=nrow<N and 0<=ncol<N:
                if l[nrow][ncol]==".":
                    if ((nrow,ncol,u[2]) not in level or level[(nrow,ncol,u[2])]>level[u]):
                        level[(nrow,ncol,u[2])]=level[u]
                        parent[(nrow,ncol,u[2])]=u
                        next.append((nrow,ncol,u[2]))
                elif l[nrow][ncol]=="!":
                    if (nrow, ncol, (u[2]+1)%4) not in level or level[(nrow, ncol, (u[2]+1)%4)] > level[u]+1:
                        level[(nrow, ncol, (u[2]+1)%4)] = level[u]+1
                        parent[(nrow, ncol, (u[2]+1)%4)]=u
                        next.append((nrow, ncol, (u[2]+1)%4))
                    if (nrow, ncol, (u[2]-1)%4) not in level  or level[(nrow, ncol, (u[2]-1)%4)] > level[u]+1:
                        level[(nrow, ncol, (u[2] - 1) % 4)] = level[u] + 1
                        parent[(nrow, ncol, (u[2] - 1) % 4)] = u
                        next.append((nrow, ncol, (u[2] - 1) % 4))
                    if ((nrow,ncol,u[2]) not in level or level[(nrow,ncol,u[2])]>level[u]):
                        level[(nrow,ncol,u[2])]=level[u]
                        parent[(nrow, ncol, u[2])] = u
                        next.append((nrow,ncol,u[2]))
                elif l[nrow][ncol]=="#" and nrow==sharp[1][0]  and ncol==sharp[1][1]:
                    ans=min(ans,level[u])
        frontier=next
        #display(next)
    return ans
print(BFS(sharp))