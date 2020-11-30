gcd=lambda c,d:c if d==0 else gcd(d,c%d)
while True:
    a,b=map(int,input().split())
    if a==0 and b==0:
        break
    temp=gcd(a,b)
    if temp==1:
        print("neither")
    elif temp==a:
        print("factor")
    else:
        print("multiple")