import itertools
l=[-1]
while True:
    l.append(list(map(int,input().split())))
    if l[-1]==[0]:
        break
    for i in itertools.combinations(l[-1][1:],r=6):
        for j in i:
            print(j,end=" ")
        print()
    print()