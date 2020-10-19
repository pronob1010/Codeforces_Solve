s1 = input()
s2 = input()
f = 0
for i in range(1,len(s1)+1):
    if s1[i-1] == s2[len(s2)-i]:
        f = 1
    else:
        f = 0
        break

if f == 1:
    print("YES")
else:
    print("NO")