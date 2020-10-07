s = input()
o = 0
z = 0
for i in range(len(s)):
    if s[i]=='0':
        o = 0
        if z<7:
            z+=1
        if z>=7:
            break

    elif s[i] == '1':
        z = 0
        if o<7:
            o+=1
        if o>=7:
            break

if o>=7 or z>= 7:
    print("YES")
else:
    print("NO")