A=int(input())
B=int(input())
C=int(input())
s=str(A*B*C)
d={i:0 for i in range(10)}
for ch in s:
    d[ord(ch)-ord("0")]+=1
for k in sorted(d.items()):
    print(k[1])