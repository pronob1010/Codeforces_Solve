t = int(input())
r = 0
for i in range(t):
    s = input()
    for j in range(len(s)):
        if s[j-1]=='+' and s[j]=='+':
            r+=1
        elif s[j-1]=='-' and s[j]=='-':
            r-=1
print(r)