N,M=map(int,input().split())
l={i:[] for i in range(N)}
for _ in range(M):
    a,b=map(int,input().split())
    l[a-1].append(b-1)
parent={}
ans=[]
def DFS_visit(s):
    for v in l[s]:
        if v not in parent:
            parent[v]=s
            DFS_visit(v)
    ans.append(s)
def DFS():
    for s in range(N):
        if s not in parent:
            parent[s]=None
            DFS_visit(s)
DFS()
for i in reversed(ans):
    print(i+1,end=" ")