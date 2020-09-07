import collections
N,K=map(int,input().split())
visit = {N:0}
parent = {N: None}
def BFS():
    frontier=collections.deque()
    frontier.append((N,0))
    while frontier:
        u=frontier.popleft()
        for v in [u[0]-1,u[0]+1,2*u[0]]:
            if v==K:
                parent[v] = u[0]
                return u[1]+1
            if 0<=v<=100001 and v not in visit:
                visit[v]=True
                parent[v]=u[0]
                frontier.append((v,u[1]+1))
if N==K:
    print(0)
    print(N)
else:
    print(BFS())
    start=K
    path=[]
    while parent[start]!=None:
        path.append(start)
        start=parent[start]
    path.append(N)
    for i in reversed(path):
        print(i,end=" ")