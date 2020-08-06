N=int(input())
#111 001 100
#001+1 00+00 100+1 11+00 111+1
a,b=0,1
for i in range(N):
    a,b=b%15746,(a+b)%15746
print(b%15746)
