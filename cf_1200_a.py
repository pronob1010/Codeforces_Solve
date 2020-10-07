n1 = int(input())

n =  [int(0) for i in range(10)]

st = input()
for i in range(len(st)):
    if st[i] == 'L':
        for j in range(len(n)):
            if n[j] is 0:
                n[j] = 1
                break

    elif st[i] is 'R':
        for j in reversed(range(len(n))):
            if n[j] is 0:
                n[j] = 1
                break

    elif int(st[i])>=0 or int(st[i])<10:
        n[int(st[i])] = 0
for i in range(len(n)):
    print(n[i],end="")
