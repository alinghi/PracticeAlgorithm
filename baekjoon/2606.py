N=int(input())
edge=int(input())
Adj=[[False]*N for _ in range(N)]
minus_int=lambda x:int(x)-1
for _ in range(edge):
    a,b=map(minus_int,input().split())
    Adj[a][b]=True
    Adj[b][a]=True
parent={0:None}
def DFS_visit(Adj,s):
    for idx,v in enumerate(Adj[s]):
        if v and idx not in parent:
            parent[idx]=s
            DFS_visit(Adj,idx)
DFS_visit(Adj,0)
print(len(parent)-1)