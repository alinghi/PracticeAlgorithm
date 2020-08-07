import itertools
N=int(input())
A,B,C,D=[0]*N,[0]*N,[0]*N,[0]*N
for i in range(N):
	A[i],B[i],C[i],D[i]=map(int,input().split())
ans=0
E=[A[i]+B[j] for i in range(N) for j in range(N)]
F=[C[i]+D[j] for i in range(N) for j in range(N)]
Etracker=0
Ftracker=N*N-1
E,F=sorted(E),sorted(F)
while Etracker<N*N and Ftracker>=0:
	if E[Etracker]+F[Ftracker]==0:
		Ecount,Fcount=0,0
		while Etracker+Ecount<N*N and E[Etracker]==E[Etracker+Ecount]:
			Ecount+=1
		while Ftracker + Fcount>=0 and F[Ftracker] == F[Ftracker + Fcount]:
			Fcount-=1
		ans+=(Ecount*-1*Fcount)
		Etracker+=Ecount
		Ftracker-=Fcount
	elif E[Etracker]+F[Ftracker]<0:
		Etracker+=1
	else:
		Ftracker-=1
print(ans)