s1 = input()
s2 = input()


for j in range(len(s2)-1):
    t = s2[0]
    s2 = s2[1:]+t
    # print(s2)
    if s1 == s2:
        print("YES")
        break

else:
    print("NO")
