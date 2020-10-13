for _ in range(int(input())):
    s = list(map(int, input().split()))
    s.sort()
    # a = s[2]
    # b = s[0]-s[1])
    # c = abs(s[1]-s[2])
    if s[1]==s[2]:
        print("YES")
        print(s[2],s[0],s[0])
    else:
        print("NO")
