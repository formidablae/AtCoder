N = int(input())
strs = set()
for tc in range(N):
    S = input()
    strs.add(S)
flag = False
for s in strs:
    if s[0] != "!" and "!" + s in strs:
        print(s)
        flag = True
        break
    elif s[0] == "!" and s[1:len(s)] in strs:
        print(s[1:len(s)])
        flag = True
        break
if not flag:
    print("satisfiable")

