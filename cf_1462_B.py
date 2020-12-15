
p = int(input())
for l in range(p):
    n = int(input())
    s = input()
    s2 = []
    c  = 0

    j = 0
    if s[j]=='2' and s[j+1]=='0' and s[j+2]=='2' and s[j+3]=='0':
        print("YES")
    elif s[j] == '2' and s[j + 1] == '0' and s[j+2] == '2' and s[n - 1] == '0':
        print("YES")
    elif s[j]=='2' and s[j+1]=='0' and s[n-2]=='2' and s[n-1]=='0':
        print("YES")

    elif s[j]=='2' and s[n-3]=='0' and s[n-2]=='2' and s[n-1]=='0':
        print("YES")
    elif s[n-4]=='2' and s[n-3]=='0' and s[n-2]=='2' and s[n-1]=='0':
        print("YES")

    else:
        print("NO")
