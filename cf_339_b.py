a,b = list(map(int, input().split()))
s = list(map(int, input().split()))[:b]
if s[0]!= 1:
    r = s[0]
else:
    r = 0
for i in range(2, len(s)):
    if s[i-1]==s[i]:
        r+=0
    elif s[i-1]>s[i]:
        r += s[i-1]
    elif s[i-1]<s[i]:
        r+=(a-s[i-2])+s[i-1]


print(r)


# c = []
# m = max(s)
# i=0
# r = 0
# while len(c)!=len(s):
#     if s[i] not in c:
#         c.append(s[i])
#     else:
#         c.append(1)
#     i+=1
# print(c)
# print(sum(c))
