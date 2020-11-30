N,M=map(int,input().split())
Adj=[[False]*N for _ in range(N)]
minus_int=lambda x:int(x)-1
for _ in range(M):
    a,b=map(minus_int,input().split())
    Adj[a][b]=True
    Adj[b][a]=True
#parent={0:None}
def DFS(Adj):
    parent={}
    connected=0
    for s in range(N):
        if s not in parent:
            parent[s]=None
            DFS_visit(Adj,s,parent)
    for i in parent:
        if parent[i]==None:
            connected+=1
    return connected
def DFS_visit(Adj,s,parent):
    for idx,v in enumerate(Adj[s]):
        if v and idx not in parent:
            parent[idx]=s
            DFS_visit(Adj,idx,parent)
print(DFS(Adj))