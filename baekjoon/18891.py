n,v=map(int,input().split())
R,N=253,300
l,ri,voted,total=[list(input().split()) for _ in range(n)],[0]*n,[0]*n,0
list_of_all_party=[]
for i in range(n):
    l[i][1],l[i][2]=map(int,l[i][1:])
    ri[i],voted[i]=l[i][1],l[i][2]
    list_of_all_party.append(l[i][0])
    total+=l[i][2]
def possible():
    pos=[voted[i]/total for i in range(n)]
    pos=[True if pos[i]>=0.03 or ri[i]>=5 else False for i in range(n)]
    return pos
pos=possible()
voted_possible=[voted[i] if pos[i] else 0 for i in range(n)]
percentage_possible=[vote/sum(voted_possible) for vote in voted_possible]
for i in range(n):
    if pos[i]:
        R-=ri[i]
def step1():
    x=N-R
    seats=[(x*percentage_possible[i]-ri[i])/2 for i in range(n)]
    calc=lambda x:0 if x<1 else round(x)
    seats=list(map(calc,seats))
    return seats
def step2a(seat1):
    x=30-sum(seat1)
    xs=[percentage_possible[i]*x for i in range(n)]
    xs_int=[int(xs[i]) for i in range(n)]
    seat2=xs_int[:]
    if sum(seat2)==x:
        seat2=[seat1[i]+seat2[i] for i in range(n)]
        return seat2
    else:
        while sum(seat2)<x:
            xs=[xs[i]-int(xs[i]) for i in range(n)]
            z=xs.index(max(xs))
            seat2[z]+=1
            xs[z]=0
        seat2 = [seat1[i] + seat2[i] for i in range(n)]
        return seat2
def step2b(seat1):
    x=sum(seat1)
    ratio=30/x
    xs=[ratio*seat1[i] for i in range(n)]
    xs_int = [int(xs[i]) for i in range(n)]
    seat2 = xs_int[:]
    if sum(seat2) == 30:
        return seat2
    else:
        while sum(seat2)<30:
            xs=[xs[i]-int(xs[i]) for i in range(n)]
            z=xs.index(max(xs))
            seat2[z]+=1
            xs[z]=0
        return seat2
def step3():
    x=17
    xs=[percentage_possible[i]*x for i in range(n)]
    xs_int = [int(xs[i]) for i in range(n)]
    seat3 = xs_int[:]
    if sum(seat3) == 17:
        return seat3
    else:
        while sum(seat3)<17:
            xs=[xs[i]-int(xs[i]) for i in range(n)]
            z=xs.index(max(xs))
            seat3[z]+=1
            xs[z]=0
        return seat3

seat1=step1()
temp=sum(seat1)
if temp>30:
    seat2=step2b(seat1)
elif temp==30:
    seat2=seat1
else:
    seat2=step2a(seat1)
seat3=step3()
final=[]
for i in range(n):
    final.append((list_of_all_party[i],ri[i]+seat2[i]+seat3[i]))
final.sort(key=lambda x:(-x[1],x[0]))
for i in range(n):
    print(final[i][0],final[i][1])
