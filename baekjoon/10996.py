N=int(input())
for x in range(N):
    for i in range((N+1)//2):
        print("* ",end="")
    print()
    for j in range((N)//2):
        print(" *",end="")
    print()