N=int(input())
people={}
for _ in range(N):
	name, order=input().split()
	if order=="enter":
		people[name]=True
	else:
		people[name]=False
l=[name for name in people.keys() if people[name]]
l.sort(reverse=True)
for i in l:
	print(i)