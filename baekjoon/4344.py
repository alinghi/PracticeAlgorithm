TC=int(input())
for _ in range(TC):
    l=list(map(int,input().split()))
    l=l[1:]
    average=sum(l)/len(l)
    count=0
    for i in l:
        if i>average:
            count+=1
    print(str('%.3f' % round(count / len(l) * 100, 3)) + '%')