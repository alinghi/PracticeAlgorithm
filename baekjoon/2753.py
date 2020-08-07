y=int(input())
ans=1 if y%400==0 else 1 if y%4==0 and y%100!=0 else 0
print(ans)