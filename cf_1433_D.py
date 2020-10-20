for i in range(int(input())):
    n = int(input())
    s = list(map(int, input().split()))
    l = len(s)

    nl = []
    for j in range(2,l+1):
        if s[j-2]!=s[j-1]:
            p = ''.join([str(j-1),' ',str(j)])
            print(p)
            nl.append(p)
    # else:
    #     print("NO")

    print(nl)
    print(len(nl))