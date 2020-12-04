t = int(input())
for i in range(t):
    n, m = list(map(int, input().split()))
    s1 = list(map(int, input().split()))
    s2 = list(map(int, input().split()))

    s1 = set(s1)
    s2 = set(s2)
    c = 0
    for i in s1:
        if i in s2:
            c+=1
    print(c)