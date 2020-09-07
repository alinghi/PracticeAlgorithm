def init(N):
    l=[list(map(int,input().split())) for _ in range(N)]
    return l
left=[3,0,1,2]
dR=[-1,0,1,0]
dC=[0,1,0,-1]

def solver():
    N, M = map(int,input().split())
    #direction 0 north 1 east 2 south 3 west
    robotR, robotC, direction = map(int,input().split())
    l=init(N)

    def simulator(l,R,C,direction):
        ans=0
        gameOver=False
        while not gameOver:
            check=False
            if l[R][C]!=2:
                l[R][C]=2
                ans=ans+1
            for i in range(4):
                direction=(direction-1)%4
                if l[R+dR[direction]][C+dC[direction]]==0:
                    R=R+dR[direction]
                    C=C+dC[direction]
                    check = True
                    break
            #Go Back, direction maintain
            if not check:
                if l[R-dR[direction]][C-dC[direction]]==1:
                    gameOver=True
                else:
                    R=R-dR[direction]
                    C=C-dC[direction]
        return ans
    ans=simulator(l,robotR,robotC,direction)
    print(ans)
solver()