
for i in range(int(input())):
    f = 0
    n = int(input())
    s = list(map(int, input().split()))

    if s[0]+s[1]>s[len(s)-1]:
        print("-1")
    else:
        print("1",end=" ")
        print("2",end=" ")
        print(n)