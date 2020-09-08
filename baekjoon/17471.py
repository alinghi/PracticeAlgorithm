import itertools
N=int(input())
population=list(map(int,input().split()))
graph=[[False]*N for _ in range(N)]
for i in range(N):
    graph[i][i]=True

def split(j):
    team1=list(j)
    team2=[]
    for i in range(N):
        if i not in team1:
            team2.append(i)
    return team1, team2
def calc(team1,team2):
    #print("---------")
    #print(team1,team2)
    graph1=[[graph[i][j] for i in team1] for j in team1]
    graph2 = [[graph[i][j] for i in team2] for j in team2]
    #print(graph1)
    #print(connected(graph1))
    #print(graph2)
    #print(connected(graph2))
    if not connected(graph1):
        return 9e9
    if not connected(graph2):
        return 9e9
    pop1,pop2=0,0
    for i in team1:
        pop1+=population[i]
    for i in team2:
        pop2+=population[i]
    return abs(pop1-pop2)
def connected(graph):
    n=len(graph)
    visited=[False]*n
    frontier=[0]
    #we do BFS here
    while frontier:
        next=[]
        for u in frontier:
            for v in range(n):
                if graph[u][v] and not visited[v]:
                    visited[v]=True
                    next.append(v)
        frontier=next
    if all(visited):
        return True
    else:
        return False

for i in range(N):
    a=list(map(int,input().split()))
    for j in range(1,len(a)):
        graph[i][a[j]-1]=True
        graph[a[j] - 1][i] = True
ans=9e9
for i in range(1, N//2+1 if N%2==0 else N//2+2):
    for j in itertools.combinations(range(N),i):
        team1,team2=split(j)
        ans=min(calc(team1,team2),ans)
if ans==9e9:
    ans=-1
print(ans)