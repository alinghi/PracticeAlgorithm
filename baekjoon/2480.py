l=list(map(int,input().split()))
l.sort()
if l[0]==l[2]:
    print(10000+l[0]*1000)
elif l[0]==l[1]:
    print(1000+l[0]*100)
elif l[1]==l[2]:
    print(1000+l[1]*100)
else:
    print(100*l[2])
