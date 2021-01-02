t = int(input())
for i in range(t):
    s = input()
    for j in range(len(s)):
        if s[j]=='R':
             print('S',end="")
        elif s[j]=='P':
            print('R',end="")
        elif s[j]=='S':
            print('P',end="")
    print()

