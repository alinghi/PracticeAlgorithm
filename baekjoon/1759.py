N,M=map(int,input().split())
l=input().split()
l.sort()
pw_list=[]
vowel=("a","e","i","o","u")
def password(current_pw,idx):
    next_pw=current_pw+l[idx]
    if len(next_pw)==N:
        n_vowel = 0
        for v in vowel:
            n_vowel += next_pw.count(v)
        if n_vowel >= 1 and N - n_vowel >= 2:
            pw_list.append(next_pw)
        return
    for next_idx in range(idx+1,M):
        password(next_pw,next_idx)
for i in range(M):
    password("",i)
for pw_cand in pw_list:
    print(pw_cand)