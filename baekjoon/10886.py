N=int(input())
print("Junhee is cute!" if sum(int(input()) for _ in range(N))>(N//2) else "Junhee is not cute!")