N=int(input())
s=[]
for _ in range(N):
    s.append(input())
for ss in s:
    l=[]
    for i in ss:
        if i==" ":
            while len(l)>0:
                print(l[-1],end="")
                l.pop()
            print(" ",end="")
        else:
            l.append(i)
    while len(l) > 0:
        print(l[-1], end="")
        l.pop()
    print()
