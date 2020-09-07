N,M=map(int,input().split())
l=[list(map(int,input().split())) for _ in range(N)]
tetris0=[[(0,1),(0,2),(0,3)]] #0,3,(0,0),add
tetris1=[[(1,0),(2,0),(3,0)]] #3,0,(0,0),add
tetris2=[[(1,0),(0,1),(1,1)]] #1,1,(0,0),add
tetris3=[[(0,0),(2,1)],[(0,1),(2,0)],[(0,0),(2,0)],[(0,1),(2,1)],
		 [(0,1),(1,1)],[(0,0),(1,0)],[(1,0),(2,0)],[(1,1),(2,1)]] #2,1,+,sub
tetris4=[[(0,0),(1,2)],[(0,2),(1,0)],[(0,0),(0,2)],[(1,0),(1,2)],
		 [(0,0),(0,1)],[(0,1),(0,2)],[(1,0),(1,1)],[(1,1),(1,2)]] #1,2,+,sub
ans,add,sub=0,lambda x,y:x+y,lambda x,y:x-y
def area(row_co,col_co,tetris_blocks,default_block,op):
	global ans
	for row in range(N-row_co):
		for col in range(M-col_co):
			s=0
			for tetris in default_block:s += l[row + tetris[0]][col + tetris[1]]
			for tetris_block in tetris_blocks:
				temp=s
				for tetris in tetris_block:	temp=op(temp,l[row+tetris[0]][col+tetris[1]])
				if ans<temp:ans=temp
operators = [(0,3,tetris0,[(0,0)],add),(3,0,tetris1,[(0,0)],add), (1,1,tetris2,[(0,0)],add),
			 (2,1,tetris3,[(0,0),(0,1),(1,0),(1,1),(2,0),(2,1)],sub), (1,2,tetris4,[(0,0),(0,1),(0,2),(1,0),(1,1),(1,2)],sub)]
for operator in operators:
	area(operator[0],operator[1],operator[2],operator[3],operator[4])
print(ans)