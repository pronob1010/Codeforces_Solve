n = int(input())
f = 0
c = "|"
ans = []
for i in range(n):
    a,b = input().split('|')
    # for j in range(len(a)):
    #     if (a[j] == 'O'):
    #         a.replace('O', 'r')
    #         print(a)

    if ((f == 0) and (a[0]== 'O' and a[1] == 'O')):
        x = a.replace('O', '+')
        f = 1
        p = x+c+b


    elif((f == 0) and (b[0]== 'O' and b[1] == 'O')):
        x = b.replace('O','+')
        f = 1
        p = a+c+x


    else:
        p = a+c+b
    ans.append(p)

if f == 0:
    print('NO')
else:
    print('YES')
    print(*ans, sep="\n")