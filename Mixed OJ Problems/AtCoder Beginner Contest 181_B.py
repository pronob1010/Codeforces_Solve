p = int(input())
r = 0
for i in range(p):
    a, n = list(map(int, input().split()))
    # for i in range(a,b+1):
    #     r += i
    r = ((n-a-1)*((n-a-1)+1))//2

print(r)