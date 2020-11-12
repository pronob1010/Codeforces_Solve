x = int(input())
n = list(map(int, input().split()))

for i in range(1,len(n)+1):
    if n[i-1]>n[i]:
        n[i - 1],n[i] = n[i],n[i-1]
        break

s  = reversed(n)


if s == n.sort():
    print(s)
    print(n)
    print("yes")
    print(s[0], s[1])
else:
    print("no")