import re
N=int(input())
for _ in range(N):
    orders=input();input();s=input()
    orders=re.sub("R{2}","",orders)
    s=(s[1:-1])
    if len(s):
        s=s.split(",")
    else:
        s=[]
    n=len(s)
    drop=orders.count("D")
    ret=True
    if drop>n:
        print("error")
        continue
    a, b = 0, 0
    for order in orders:
        if order=="R":
            ret=1-ret
        else:
            if ret:
                a+=1
            else:
                b-=1
    if b==0:
        s=s[a:]
    else:
        s=s[a:b]
    z = "["
    if ret:
        for ch in s:
            z = z + ch + ","
    else:
        for ch in reversed(s):
            z = z + ch + ","
    if len(z)>1:
        print(z[:-1],end="")
        print("]")
    else:
        print("[]")