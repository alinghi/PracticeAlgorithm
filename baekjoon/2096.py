N=int(input())
dpmin=tuple(map(int,input().split()))
dpmax=dpmin
for i in range(1,N):
    l = tuple(map(int, input().split()))
    dpmin=(min(dpmin[0],dpmin[1])+l[0], min(dpmin[0], dpmin[1],dpmin[2]) + l[1], min(dpmin[1], dpmin[2]) + l[2])
    dpmax=(max(dpmax[0], dpmax[1]) + l[0], max(dpmax[0], dpmax[1], dpmax[2]) + l[1], max(dpmax[1], dpmax[2]) + l[2])
print(max(dpmax),min(dpmin))