a,b = list(map(int, input().split()))

for i in range(b):
    c = a%10

    if c == 0:
        a //= 10
    else:
        a = a - 1

print(a)