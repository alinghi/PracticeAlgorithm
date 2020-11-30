N,M,K=map(int,input().split())
l=[list(map(int,input().split())) for _ in range(N)]
dr,dc=(-1,1,0,0),(0,0,-1,1)

fish={}
for i in range(N):
    for j in range(N):
        if l[i][j]:fish[l[i][j]-1]=(i,j)
minus_int=lambda x:int(x)-1
first_direction=list(map(minus_int,input().split()))
for i in range(M):fish[i]=fish[i]+tuple([first_direction[i]])
priority_direction=[[list(map(minus_int,input().split())) for _ in range(4)] for fishes in range(M)]

def simulator(fishes,priority_direction):
    m=[[None]*N for _ in range(N)]
    def display(text):
        print("=======================",text)
        for i in range(N):
            for j in range(N):
                if m[i][j]:
                    print(str(m[i][j][0]+1).zfill(2),str(m[i][j][1]).zfill(2),end=" ")
                else:
                    print("-----",end=" ")
            print()
        print(fishes)
        print("# of fish, ",len(fishes))
    def diffuse():
        for fish in fishes.items():
            fish_number,fish_row,fish_col,fish_direction=fish[0],fish[1][0],fish[1][1],fish[1][2]
            m[fish_row][fish_col]=(fish_number,K)
    def decrease():
        for row in range(N):
            for col in range(N):
                if m[row][col]:
                    if m[row][col][1]==1:
                        m[row][col]=None
                    else:
                        m[row][col]=(m[row][col][0],m[row][col][1]-1)
    def move():
        l=[[[] for _ in range(N)] for i in range(N)]
        for fish in fishes.items():
            fish_number,fish_row,fish_col,fish_direction=fish[0],fish[1][0],fish[1][1],fish[1][2]
            directions=priority_direction[fish_number][fish_direction]
            cand=[]
            for direction in directions:
                nrow,ncol=fish_row+dr[direction],fish_col+dc[direction]
                if 0<=nrow<N and 0<=ncol<N and not m[nrow][ncol]:
                    cand.append((nrow,ncol,direction))
                    break
            if not cand:
                for direction in directions:
                    nrow, ncol = fish_row + dr[direction], fish_col + dc[direction]
                    if 0 <= nrow < N and 0 <= ncol < N and m[nrow][ncol]:
                        m_fish_number,age=m[nrow][ncol][0],m[nrow][ncol][1]
                        if m_fish_number==fish_number:
                            cand.append((nrow,ncol,direction))
                            break
            nrow,ncol,ndirection=cand[0]
            fishes[fish_number]=(nrow,ncol,ndirection)
            l[nrow][ncol].append(fish_number)
        for row in range(N):
            for col in range(N):
                if len(l[row][col])>1:
                    temp=min(l[row][col])
                    l[row][col].remove(temp)
                    for deleted in l[row][col]:
                        del fishes[deleted]
    time=0
    while len(fish)!=1 and time<1001:
        diffuse()
        move()
        decrease()
        time+=1
    return -1 if time==1001 else time

print(simulator(fish,priority_direction))