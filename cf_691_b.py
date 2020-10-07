s = input()

p=[]
for i in reversed(range(len(s))):
    p.append(s[i])

f = 0
for i in range(len(s)):
    if s[i] is p[i]:
        f = 1
        break



if f == 1:
    print("NIE")
else:
    print("TAK")