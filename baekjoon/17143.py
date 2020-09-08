R,C,M=map(int,input().split())
dir=[-1,0,2,3,1]
dR=[-1,0,1,0]
dC=[0,-1,0,1]
# 0row 1col 2speed 3direction 4size
sharks=[list(map(int,input().split())) for _ in range(M)]
def pick(sharks,naksi):
	minimum=987654321
	index=-1
	weight=-1
	for i in range(len(sharks)):
		if sharks[i][1]==naksi:
			if minimum>sharks[i][0]:
				minimum=sharks[i][0]
				index=i
				weight=sharks[i][4]
	if index==-1:
		return 0
	else:
		sharks.pop(index)
		return weight

def moves(sharks,row,col):
	for shark in sharks:
		move(shark,row,col)


def move(shark,row,col):
	for _ in range(shark[2]):
		nR,nC=shark[0]+dR[shark[3]],shark[1]+dC[shark[3]]
		if 0<=nR<row and 0<=nC<col:
			shark[0],shark[1]=nR,nC
		else:
			shark[3]=(shark[3]+2)%4
			nR, nC = shark[0] + dR[shark[3]], shark[1] + dC[shark[3]]
			shark[0], shark[1] = nR, nC
def kills(sharks):
	kill=[]
	count=0
	for i in range(len(sharks)-1):
		if sharks[i][0]==sharks[i+1][0] and sharks[i][1]==sharks[i+1][1]:
			kill.append(i+1)
	for i in kill:
		sharks.pop(i+count)
		count=count-1



ans=0
for i in range(len(sharks)):
	for k in range(2):
		sharks[i][k]=sharks[i][k]-1
	sharks[i][3]=dir[sharks[i][3]]
for naksi in range(C):
	ans+=pick(sharks,naksi)
	moves(sharks,R,C)
	sharks = sorted(sharks, key=lambda x: (x[0], x[1], -x[4]))
	kills(sharks)
print(ans)