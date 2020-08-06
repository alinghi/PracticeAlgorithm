a = [int(input()) for _ in range(9)]
aim=sum(a)-100
a.sort()
def solve():
    for i in range(9):
        for j in range(i+1,9):
            if aim==a[i]+a[j]:
                for k in range(9):
                    if k==i or k==j:
                        continue
                    else:
                        print(a[k])
                return
solve()