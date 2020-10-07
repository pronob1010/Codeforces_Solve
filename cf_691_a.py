li = []
n = int(input())
s = list(map(int,input().strip().split()))[:n]
# li = [int(i) for i in s]
# li.reverse()
f = 0

for i in range(len(s)):
    if s[i] is 1:
        li.append(s[i])

if len(li)>0:
    if len(s)> 1 and (len(li) == len(s)):
        print('NO')
    elif len(s) is 1 and (len(li) == len(s)):
        print('YES')
    elif len(li) == (len(s)-1):
        print("YES")
    else:
        print('NO')
else:
    print('NO')