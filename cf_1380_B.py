t = int(input())
for i in range(t):
    s = input()
    fre = {}
    for j in range(len(s)):
        if s[j] in fre:
            fre[s[j]]+=1
        else:
            fre[s[j]]=1
    max_latter = max(fre, key=fre.get)
    max_value = max(fre.values())

    # for k in range(len(s)):
    #     if max_latter=='R' and s[k]=='R':
    #         s2 += 'P'
    #     elif max_latter=='P':
    #         s2 += 'S'
    #     elif max_latter=='S':
    #         s2 += 'R'
    #     else:
    #         s2+=s[k]
    # # for k in range(len(s)-max_value):
    # #     s2+='R'
    #
    # # print(max_latter,max_value)
    #
    # # new_string = ''.join()
    # print(s2)


    if max_latter=='R':
        s2 = 'P'*len(s)
    elif max_latter=='P':
        s2 = 'S'*len(s)
    elif max_latter=='S':
        s2 = 'R'*len(s)


    # print(max_latter,max_value)

    # new_string = ''.join()
    print(s2)
