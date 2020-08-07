N=int(input())
l=[]
for _ in range(N):
	m,c,i=map(int,input().split())
	program=input()
	data=input()
	l.append([m,c,i,program,data])
for tc in l:
	infinite=False
	mem=[0]*tc[0]
	m,c,data_len,program,data=tc
	memory_pointer=0
	program_counter=0
	input_counter=0
	max_idx=0
	super_counter=0
	#loop check
	stack=[]
	loop=dict()
	for i in range(c):
		if program[i]=='[':
			stack.append(i)
		if program[i]==']':
			loop[stack[-1]]=i
			loop[i]=stack[-1]
			stack.pop()
	#execute
	program_counter=0
	while program_counter<c:
		if program[program_counter]=='-':
			mem[memory_pointer]=(mem[memory_pointer]-1)%256
			program_counter=program_counter+1
		elif program[program_counter]=='+':
			mem[memory_pointer] = (mem[memory_pointer] + 1) % 256
			program_counter=program_counter+1
		elif program[program_counter] == '<':
			memory_pointer=(memory_pointer-1)%m
			program_counter=program_counter+1
		elif program[program_counter] == '>':
			memory_pointer = (memory_pointer + 1) % m
			program_counter=program_counter+1
		elif program[program_counter] == '[':
			if mem[memory_pointer]==0:
				program_counter=loop[program_counter]
			else:
				program_counter=program_counter+1
		elif program[program_counter] == ']':
			if mem[memory_pointer]!=0:
				program_counter=loop[program_counter]
			else:
				program_counter=program_counter+1
		elif program[program_counter] == '.':
			#print(chr(mem[memory_pointer]))
			program_counter=program_counter+1
		elif program[program_counter] == ',':
			if input_counter>data_len-1:
				mem[memory_pointer]=255
			else:
				mem[memory_pointer]=ord(data[input_counter])
				input_counter=input_counter+1
			program_counter = program_counter + 1
		max_idx=max(program_counter,max_idx)
		super_counter=super_counter+1
		if super_counter>50000000:
			infinite=True
			break
	if infinite:
		print("Loops {} {}".format(loop[max_idx],max_idx))
	else:
		print("Terminates")