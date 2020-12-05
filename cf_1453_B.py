t = int(input())
for i in range(t):
    n = int(input())
    s = list(map(int, input().split()))
    s.sort()
    mi = min(s)
    mx = max(s)
    print(s)

    # j = 0
    # while mi != mx:
    #     j+=1
    #     mi+=1
    # print(j)