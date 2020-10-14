n = int(input())
s = input()
neig = 0
for i in range(1,n):
    if s[i-1]==s[i] and s[i-1]=='R':
        neig +=1
    elif s[i-1]==s[i] and s[i-1]=='G':
        neig +=1
    elif s[i-1]==s[i] and s[i-1]=='B':
        neig +=1

print(neig)
