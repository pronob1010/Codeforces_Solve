n = int(input())
s = list(map(int, input().split()))[:n]
m = max(s)
min = min(s)
print(m,min)
if n == 2 or (s[0]==m and s[len(s)-1]==min):
    if s[0]>s[len(s)-1]:
        print('0')
    else:
        print('1')
else:
    for i in range(1,len(s)):
        if s[i]==m:
            mp = i+1
    for i in range(1,len(s)):
        if s[i]==min:
            minp = i+1

    print(minp,mp)
    t = (mp-1)+(len(s)-minp)
    if n%2==0:
        print(t)
    else:
        print(t-1)

# # print(s[len(s)-1])
# c = 0
# i=2
# while (not(s[0]==m and s[len(s)-1]==min)):
#     if s[i-2] < s[i-1]:
#         t = s[i-2]
#         s[i-2] = s[i-1]
#         s[i-1] = t
#         c += 1
#     if i<len(s):
#         i+=1
#     else:
#
#         i=2
#     print(s)
# print(c)
