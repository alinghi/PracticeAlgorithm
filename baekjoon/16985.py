import itertools
def rotate55(l): #clockwise 90 degree rotate
    return [[l[4-j][i] for j in range(5)] for i in range(5)]
def cubemaker(m,disc_orders,disc_selections):
    cube=[]
    for i,disc_order in enumerate(disc_orders):
        cube.append(m[disc_order*4+disc_selections[i]])
    return cube
dx=(1,-1,0,0,0,0)
dy=(0,0,1,-1,0,0)
dz=(0,0,0,0,1,-1)
def calc(cube):
    #in case of entry or exit is blocked
    if cube[0][0][0]==0 or cube[4][4][4]==0:
        return 9e9
    level={(0,0,0):0}
    i=1
    frontier=[(0,0,0)]
    while frontier:
        next=[]
        for x,y,z in frontier:
            for direction in range(6):
                nx,ny,nz=x+dx[direction],y+dy[direction],z+dz[direction]
                if 0<=nx<5 and 0<=ny<5 and 0<=nz<5 and cube[nx][ny][nz]==1 and (nx,ny,nz) not in level:
                    if nx==4 and ny==4 and nz==4:
                        return i
                    level[(nx,ny,nz)]=i
                    next.append((nx,ny,nz))
        frontier=next
        i=i+1
    return 9e9

l=[[list(map(int,input().split())) for _ in range(5)] for _ in range(5)]
m=[]
for l_idx in range(5):
    idx=l[l_idx]
    for rotate in range(4):
        m.append(idx)
        idx=rotate55(idx)

def solution():
    ans = 9e9
    for disc_orders in itertools.permutations(range(5)):
        for disc_selections in itertools.product(range(4),repeat=5):
            cube=cubemaker(m,disc_orders,disc_selections)
            temp=calc(cube)
            if temp==12:
                return 12
            ans=min(ans,temp)
    return -1 if ans==9e9 else ans
print(solution())