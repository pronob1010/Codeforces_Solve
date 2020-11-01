t = int(input())
for i in range(t):
    a, b, c, d = list(map(int, input().split()))
    print(max((a+b),(c+d)))