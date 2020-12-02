s1 = input()
s2 = input()
x = sorted(s1)
y = sorted(s2)
c = 0
if x == y :
    for i in range(len(x)):
        if s1[i]!= s2[i]:
            c+=1
    if c == 2:
        print("YES")
    else:
        print("NO")
else:
    print("NO")
