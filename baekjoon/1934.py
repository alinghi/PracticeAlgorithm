N=int(input())
def gcd(a,b):
    if b>a:
        return gcd(b,a)
    elif b==0:
        return a
    else:
        return gcd(b,a%b)
for i in range(N):
    a,b=map(int,input().split())
    print(a*b//gcd(a,b))