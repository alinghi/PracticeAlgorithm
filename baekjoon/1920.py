N=int(input())
A=list(map(int,input().split()))
A.sort()
N=int(input())
B=list(map(int,input().split()))
def binarySearch(i):
	low=0
	high=len(A)-1
	while low<=high:
		mid=(low+high)//2
		if A[mid]==i:
			return 1
		elif A[mid]<i:
			low=mid+1
		else:
			high=mid-1
	return 0

for i in B:
	print(binarySearch(i))