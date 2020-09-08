N,M=map(int,input().split())
l={i:i for i in range(1,100)}
for _ in range(N+M):
    a,b=map(int,input().split())
    l[a]=b
def BFS():
    parent={1:None}
    level={1:0}
    i=1
    frontier=[1]
    while frontier:
        next=[]
        for u in frontier:
            for v in [u+1,u+2,u+3,u+4,u+5,u+6]:
                if v>100:
                    continue
                if v==100:
                    return i
                if l[v] not in level:
                    level[l[v]]=i
                    parent[l[v]]=u
                    next.append(l[v])
        frontier=next
        i=i+1
print(BFS())
