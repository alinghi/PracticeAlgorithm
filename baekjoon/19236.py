dr=(-1,-1,0,1,1,1,0,-1)
dc=(0,-1,-1,-1,0,1,1,1)
move=(-4,-5,-1,3,4,5,1,-3)
dz = ('⭡','⭦','⭠','⭩','⭣','⭨','⭢','⭧')

l=[list(map(int,input().split())) for _ in range(4)]
l=[[(l[i][2*j],l[i][2*j+1]-1) for j in range(4)] for i in range(4)]
def display(boards):
    print("================")
    for row in range(4):
        for col in range(4):
            print(str(boards[row][col][0]).zfill(2),dz[boards[row][col][1]],end="  ")
        print()
def rotate(original):
    return (original[0],(original[1]+1)%8)
def move(shark_row,shark_col,boards,fish_size):
    row,col,flag=0,0,False
    for nrow in range(4):
        for ncol in range(4):
            if fish_size==boards[nrow][ncol][0]:
                row,col=nrow,ncol
                flag=True
                break
        if flag:
            break
    for i in range(8):
        #if availble swap and break
        nrow,ncol=row+dr[boards[row][col][1]],col+dc[boards[row][col][1]]
        if 0<=nrow<4 and 0<=ncol<4 and not (nrow==shark_row and ncol==shark_col):
            boards[row][col],boards[nrow][ncol]=boards[nrow][ncol],boards[row][col]
            break
        #rotate
        boards[row][col]=rotate(boards[row][col])

def go(shark_row,shark_col,shark_score,boards):
    shark_score+=boards[shark_row][shark_col][0]
    shark_direction=boards[shark_row][shark_col][1]
    boards[shark_row][shark_col]=(0,0)
    candidates=[]
    for row in range(4):
        for col in range(4):
            if boards[row][col][0]:
                candidates.append(boards[row][col][0])
    candidates.sort()
    for candidate in candidates:
        move(shark_row, shark_col, boards, candidate)
    save_boards=[row[:] for row in boards]
    ret=[]
    flag=False
    for i in range(1,4):
        new_shark_row,new_shark_col=shark_row+i*dr[shark_direction],shark_col+i*dc[shark_direction]
        if 0<=new_shark_row<4 and 0<=new_shark_col<4 and boards[new_shark_row][new_shark_col][0]>0:
            flag=True
            ret.append(go(new_shark_row, new_shark_col, shark_score, boards))
        boards=[row[:] for row in save_boards]
    if not flag:
        return shark_score
    else:
        return max(ret)
print(go(0,0,0,l))