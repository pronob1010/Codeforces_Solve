for i in range(int(input())):
    n = int(input())
    s = list(map(int, input().split()))
    # print(s)
    l = len(s)//2
    s1 = []
    s2 = []
    for j in range(l):
        print(s[j])

    for j in range(l,len(s)):
        s2.append(s[j])


    print(s1)
    print(s2)

