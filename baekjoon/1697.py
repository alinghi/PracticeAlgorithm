import collections
N,K=map(int,input().split())
def BFS():
    visit = {}
    frontier=collections.deque()
    frontier.append((N,0))
    while frontier:
        u=frontier.popleft()
        for v in [u[0]-1,u[0]+1,2*u[0]]:
            if v==K:
                return u[1]+1
            if 0<=v<=100001 and v not in visit:
                visit[v]=True
                frontier.append((v,u[1]+1))
if N==K:
    print(0)
else:
    print(BFS())