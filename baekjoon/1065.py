N=int(input())
ans=0
def indicator(i):
	if i<10:
		return True
	x=str(i)
	gongcha=ord(x[0])-ord(x[1])
	for i in range(1,len(x)-1):
		if gongcha!=ord(x[i])-ord(x[i+1]):
			return False
	return True
for i in range(1,N+1):
	ans+=indicator(i)
print(ans)