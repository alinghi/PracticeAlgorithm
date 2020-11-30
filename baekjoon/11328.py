N=int(input())
for _ in range(N):
    a,b=input().split()
    print("Possible" if "".join(sorted(a))=="".join(sorted(b)) else "Impossible")