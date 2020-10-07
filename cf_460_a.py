a, b = list(map(int, input().split()))
c = 0
if a < b:
    print(a)
else:
    while True:
        if a < b:
            break
        else:
            a = a - b
            c += 1
            a += 1

    print(c * b + a)
