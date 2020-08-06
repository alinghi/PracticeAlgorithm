import collections
import sys
sys.setrecursionlimit(10**6)

def init():
    N,M,V=map(int,input().split())
    l=[[] for _ in range(N+1)]
    for i in range(M):
        x,y=map(int,input().split())
        l[x].append(y)
        l[y].append(x)
    for i in range(N+1):
        l[i].sort()
    return N,M,V,l
def visit(N):
    l=[False] * (N+1)
    l[0]=True
    return l

def DFS(V):
    visit_dfs[V]=True
    print(V, end=" ")
    for i in l[V]:
        if not visit_dfs[i]:
            DFS(i)
def BFS(V):
    de=collections.deque()
    de.append(V)
    visit_bfs[V]=True
    while de:
        x=de.popleft()
        print(x, end=" ")
        for i in l[x]:
            if not visit_bfs[i]:
                de.append(i)
                visit_bfs[i]=True


N,M,V,l=init()
visit_dfs=visit(N)
visit_bfs=visit(N)
DFS(V)
print()
BFS(V)