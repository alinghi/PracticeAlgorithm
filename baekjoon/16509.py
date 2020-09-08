def BFS():
    level = {sang: 0}
    frontier = [sang]
    i = 1
    while frontier:
        next = []
        for u in frontier:
            for k in range(8):
                p2=(u[0]+path[k][2][0],u[1]+path[k][2][1])
                if p2==king:
                    return i
                p1 = (u[0] + path[k][1][0], u[1] + path[k][1][1])
                if p1==king:
                    continue
                p0 = (u[0] + path[k][0][0], u[1] + path[k][0][1])
                if p0==king:
                    continue
                if 0<=p2[1]<=8 and 0<=p2[0]<=9:
                    if p2 not in level:
                        level[p2]=i
                        next.append(p2)
        frontier=next
        i=i+1

path=[
    [(1,0),(2,1),(3,2)],
    [(1,0),(2,-1),(3,-2)],
    [(-1,0),(-2,1),(-3,2)],
    [(-1,0),(-2,-1),(-3,-2)],
    [(0,1),(1,2),(2,3)],
    [(0,1),(-1,2),(-2,3)],
    [(0,-1),(1,-2),(2,-3)],
    [(0,-1),(-1,-2),(-2,-3)]
]
sang=tuple(map(int,input().split()))
king=tuple(map(int,input().split()))
print(BFS())