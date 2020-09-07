def diceCounter(n):
    l=[2,3,0,1,5,4]
    return l[n]

def diceMove(diceIndex,direction):
    l=[[0,0,3,1],[5,4,0,2],[2,2,1,3],[4,5,2,0],[1,3,4,4],[3,1,5,5]]
    return l[diceIndex][direction-1]

def solver():
    N, M, diceX, diceY, K=map(int,input().split())
    l=[list(map(int,input().split())) for _ in range(N)]
    op=list(map(int,input().split()))
    dice=[0,0,0,0,0,0]
    temp=[]
    diceIndex=0
    #index 0 -> dummy!
    dX=[0,0,0,-1,1]
    dY=[0,1,-1,0,0]
    def isBoundary(diceX,diceY,direction):
        if (0<=diceX+dX[direction]<N) and (0<=diceY+dY[direction]<M):
            return True
        else:
            return False
    for direction in op:
        if isBoundary(diceX,diceY,direction):
            diceX, diceY = diceX+dX[direction], diceY+dY[direction]
            temp=dice[:]
            for i in range(6):
                dice[i]=temp[diceMove(i,direction)]
            if l[diceX][diceY]==0:
                l[diceX][diceY]=dice[1]
            else:
                l[diceX][diceY], dice[1] = 0, l[diceX][diceY]
            print(dice[3])
solver()