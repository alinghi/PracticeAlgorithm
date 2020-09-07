T=int(input())
l=[0,1,2,4]
cand=[]
for _ in range(T):
	cand.append(int(input()))
for i in range(4,max(cand)+1):
	l.append((l[-1]+l[-2]+l[-3])%1000000009)
for i in cand:
	print(l[i]%1000000009)