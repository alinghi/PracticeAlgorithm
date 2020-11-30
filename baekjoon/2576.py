l=[int(input()) for _ in range(7)]
l=[i for i in l if i%2==1]
if l:
    print(sum(l))
    print(min(l))
else:
    print(-1)