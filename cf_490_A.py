n = int(input())
s = list(map(int, input().split()))
pro = s.count(1)
math = s.count(2)
phy = s.count(3)
team = min(pro, math, phy)

print(team)
if team>0:
    ppp = []
    mmm = []
    phh = []

    for i in range(len(s)):
        if s[i] == 1:
            ppp.append(i + 1)
        elif s[i] == 2:
            mmm.append(i + 1)
        elif s[i] == 3:
            phh.append(i + 1)

    for i in range(team):
        print(ppp[i], mmm[i],phh[i])
