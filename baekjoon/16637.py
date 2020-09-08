N=int(input())
s=input()
num=tuple(map(int,s[::2]))
op=tuple(s[1::2])
if N==1:
    print(s)
else:
    f=lambda n1, op, n2: n1+n2 if op=="+" else n1-n2 if op=="-" else n1*n2
    dp=[(num[0],num[0]),(f(num[0],op[0],num[1]),f(num[0],op[0],num[1]))]
    for i in range(2,(N+1)//2):
        a,b=map(lambda z:f(z,op[i-1],num[i]),dp[-1])
        e=f(num[i-1],op[i-1],num[i])
        c, d = map(lambda z: f(z, op[i - 2], e), dp[-2])
        dp.append((min(a,b,c,d),max(a,b,c,d)))
    print(dp[-1][1])