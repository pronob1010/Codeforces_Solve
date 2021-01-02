t = int(input())
for i in range(t):
    n = int(input())
    s = list(map(int, input().split()))
    new_string = []
    for j in s:
        if j not in new_string:
            new_string.append(j)
    print(*new_string, sep=" ")

