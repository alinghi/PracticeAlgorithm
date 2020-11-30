N=int(input())
i=1
z=1
while True:
    if i*(i-1)//2+1 <=N<=i*(i+1)//2:
        break
    i+=1
    z=1-z
if z:
    print(str(i+1-(i+1+N-i*(i+1)//2-1))+"/"+str(i+1+N-i*(i+1)//2-1))
else:
    print(str(i + 1 + N - i * (i + 1) // 2 - 1)+"/"+str(i + 1 - (i + 1 + N - i * (i + 1) // 2 - 1)))