N=int(input())
one,zero,pos,neg=0,False,[],[]
for _ in range(N):
	i=int(input())
	if i==1:
		one+=1
	elif i==0:
		zero=True
	elif i>1:
		pos.append(i)
	else:
		neg.append(i)
ans,pos,neg=one,sorted(pos,key=lambda x:-x),sorted(neg)
for i in range(len(pos)//2):	ans+=pos[2*i]*pos[2*i+1]
for i in range(len(neg)//2):	ans+=neg[2*i]*neg[2*i+1]
ans+=pos[-1] if len(pos)%2==1 else 0
ans+=0 if len(neg)%2==0 else neg[-1] if not zero else 0
print(ans)