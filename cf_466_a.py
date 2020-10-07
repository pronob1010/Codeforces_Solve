n, m, a, b = list(map(int, input().split()))
cost = 0
u = b / m

if m>n and (u * m)<(a*n):
    cost += int(u * m)

elif u < a and n % m == 0:
    cost += int(u * n)

elif u < a and (n % m >=1):
    if b < a:
        n += (m - (n % m))
        cost += int(u * n)

    else:
        cost += int((u * (n - (n % m))) + (a*(n % m)))

else:
    cost += a * n

print(cost)