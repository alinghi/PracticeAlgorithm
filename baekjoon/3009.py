a,b=0,0
for _ in range(3):
    c,d=map(int,input().split())
    a,b=a^c,b^d
print(a,b)