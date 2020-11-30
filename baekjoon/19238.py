N,M,fuel=map(int,input().split())
minus_int=lambda x:int(x)-1
m=[list(map(int,input().split())) for _ in range(N)]
taxi_row,taxi_col=map(minus_int,input().split())
l=[list(map(minus_int,input().split())) for _ in range(M)]
dr,dc=(0,0,1,-1),(1,-1,0,0)
destination={}
for idx,info in enumerate(l):
    m[info[0]][info[1]]=idx+2
    destination[idx+2]=(info[2],info[3])

def simulator(taxi_row,taxi_col,fuel):
    taxi_number=M
    def BFS(t_row,t_col):
        if m[t_row][t_col]>1:
            return m[t_row][t_col], t_row, t_col,0
        frontier=[(t_row,t_col)]
        level={(t_row,t_col):0}
        parent={(t_row,t_col):None}
        i=1
        while frontier:
            next=[]
            for tr,tc in frontier:
                for v in range(4):
                    nr,nc=tr+dr[v],tc+dc[v]
                    if 0<=nr<N and 0<=nc<N and m[nr][nc]!=1 and (nr,nc) not in level:
                        level[(nr,nc)]=i
                        parent[(nr,nc)]=(tr,tc)
                        next.append((nr,nc))
            i=i+1
            candidates=[]
            for nxt in next:
                if m[nxt[0]][nxt[1]]>1:
                    candidates.append(nxt)
            if candidates:
                candidates.sort()
                return m[candidates[0][0]][candidates[0][1]], candidates[0][0], candidates[0][1], level[candidates[0]]
            frontier=next
        return -1,-1,-1,-1
    def taxing(start_row,start_col,dest_row,dest_col):
        frontier=[(start_row,start_col)]
        level={(start_row,start_col):0}
        i=1
        while frontier:
            next=[]
            for tr,tc in frontier:
                for v in range(4):
                    nr,nc=tr+dr[v],tc+dc[v]
                    if 0<=nr<N and 0<=nc<N and m[nr][nc]!=1 and (nr,nc) not in level:
                        if nr==dest_row and nc==dest_col:
                            return i
                        level[(nr,nc)]=i
                        next.append((nr,nc))
            i=i+1
            frontier=next
        return -1

    #taxi to nearest guest
    #passenger number, passenger_row, passenger_col,fuel_consumption
    while taxi_number>0:
        passenger_number,taxi_row,taxi_col,fuel_consumption=BFS(taxi_row,taxi_col)
        if passenger_number==-1:
            return -1
        m[taxi_row][taxi_col]=0
        if fuel-fuel_consumption<0:
            return -1
        fuel=fuel-fuel_consumption
        #taxi to destination
        actual_fuel=taxing(taxi_row,taxi_col, destination[passenger_number][0], destination[passenger_number][1])
        if actual_fuel==-1:
            return -1
        taxi_row,taxi_col=destination[passenger_number][0], destination[passenger_number][1]
        if fuel-actual_fuel<0:
            return -1
        fuel = fuel - actual_fuel
        fuel=fuel+actual_fuel*2
        taxi_number-=1
    return(fuel)
    #refuel
print(simulator(taxi_row,taxi_col,fuel))