A=int(input())
B=int(input())
b=B
while b>0:
    print(A*(b%10))
    b=b//10
print(A*B)