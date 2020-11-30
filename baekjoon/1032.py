N=int(input())
l=[input() for _ in range(N)]
ans=""
for word_position in range(len(l[0])):
    minus=ord(l[0][word_position])
    calc=[minus-ord(l[word_num][word_position]) for word_num in range(len(l))]
    ans+=("?" if any(calc) else l[0][word_position])
print(ans)