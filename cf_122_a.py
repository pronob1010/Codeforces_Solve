n = input()
f = 0
for i in range(len(n)):
    if n[0]== '4' or n[0]== '7':
        if n[i]=='4' or n[i] == '7':
            f=1
        else:
            break

if f == 0:
    print("NO")
else:
    print("YES")
