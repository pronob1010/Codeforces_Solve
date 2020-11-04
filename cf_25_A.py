n = int(input())
s = list(map(int, input().split()))

e = 0
odd = 0
for i in s:
    if i%2==0:
        e+=1
    else:
        odd+=1

if e > odd:
    for i in range(len(s)):
        if s[i] % 2 == 1:
            print(i+1)
            break
else:
    for i in range(len(s)):
        if s[i]%2==0:
            print(i+1)
            break
