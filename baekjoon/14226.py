N=int(input())
def BFS():
    parent={(1,0):None}
    level={(1,0):0}
    i=1
    frontier=[(1,0)]
    while frontier:
        next=[]
        for u in frontier:
            for v0,v1 in [(u[0],u[0]),(u[0]+u[1],u[1]),(u[0]-1,u[1])]:
                if v0==N:
                    return i
                else:
                    if (v0,v1) not in level:
                        level[(v0,v1)]=i
                        parent[(v0,v1)]=u
                        next.append((v0,v1))
        frontier=next
        i=i+1
print(BFS())
