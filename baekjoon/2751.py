def solver(n):
    l=[]
    for _ in range(n):
        l.append(int(input()))
    l.sort()
    for i in l:
        print(i)

n=int(input())
solver(n)