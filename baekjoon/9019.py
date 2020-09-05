from collections import deque
N=int(input())
l=[list(map(int,input().split())) for _ in range(N)]

for i in l:
    visited = [False] * 10001
    bfs=deque()
    bfs.append([i[0],""])
    visited[i[0]]=True
    while True:
        candidate=bfs.popleft()
        temp=(candidate[0]*2)%10000
        if temp==i[1]:
            print(candidate[1] + "D")
            break
        if not visited[temp]:
            bfs.append([temp, candidate[1] + "D"])
            visited[temp] = True
        temp = (candidate[0]-1)%10000
        if temp == i[1]:
            print(candidate[1] + "S")
            break
        if not visited[temp]:
            bfs.append([temp, candidate[1] + "S"])
            visited[temp] = True
        temp = (candidate[0]%1000)*10+(candidate[0]//1000)
        if temp == i[1]:
            print(candidate[1] + "L")
            break
        if not visited[temp]:
            bfs.append([temp, candidate[1] + "L"])
            visited[temp] = True
        temp = (candidate[0]//10)+(candidate[0]%10)*1000
        if temp == i[1]:
            print(candidate[1] + "R")
            break
        if not visited[temp]:
            bfs.append([temp, candidate[1] + "R"])
            visited[temp] = True