N=int(input())
for i in range(N):
    for j in range(i+1):
        print("*",end="")
    print()
for i in reversed(range(N-1)):
    for j in range(i+1):
        print("*",end="")
    print()