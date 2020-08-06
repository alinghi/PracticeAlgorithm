N=int(input())
if N==0:
    print(1)
else:
    l=[0]*10
    while N>0:
        l[N%10]+=1
        N=N//10
    a=l[6]+l[9]
    if a%2==1:
        a=a//2+1
    else:
        a=a//2
    l[6],l[9]=a,a
    print(max(l))