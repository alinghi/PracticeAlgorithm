N,M=map(int,input().split())
l=[list(input()) for _ in range(N)]
dr,dc=(0,0,1,-1),(1,-1,0,0)
Water=[]
for i in range(N):
    for j in range(M):
        if l[i][j]=="D":
            D=(i,j)
        elif l[i][j]=="S":
            l[i][j]="."
            S=(i,j)
        elif l[i][j]=="*":
            Water.append((i,j))
def BFS(D,S,Water,maps):
    l=[maps[i][:] for i in range(N)]
    #water first
    waters=Water[:]
    waters_level={water:0 for water in waters}
    water_frontier=[water for water in waters]
    i=1
    movers=S
    movers_level={S:0}
    movers_frontier=[S]
    while movers_frontier:
        next_movers=[]
        next_waters=[]
        #water first
        for water in water_frontier:
            for direction in range(4):
                water_row,water_col=water[0]+dr[direction],water[1]+dc[direction]
                if 0<=water_row<N and 0<=water_col<M and l[water_row][water_col]==".":
                    l[water_row][water_col]="*"
                    waters_level[(water_row,water_col)]=i
                    next_waters.append((water_row,water_col))
        #print(l)
        for mover in movers_frontier:
            for direction in range(4):
                mover_row,mover_col=mover[0]+dr[direction],mover[1]+dc[direction]
                if (mover_row,mover_col)==D:
                    return i
                if 0<=mover_row<N and 0<=mover_col<M and l[mover_row][mover_col]=="." \
                        and (mover_row,mover_col) not in movers_level:
                    movers_level[(mover_row,mover_col)]=i
                    next_movers.append((mover_row,mover_col))
        #print(next_movers)
        water_frontier=next_waters
        movers_frontier=next_movers
        i=i+1
    return "KAKTUS"

print(BFS(D,S,Water,l))