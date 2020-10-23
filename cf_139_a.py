n = int(input())
s = list(map(int,input().split()))
c = 0
r = 0
i = 0
while(r<n):
    c+=1
    if i<len(s):
        r+=s[i]
        # print(r,c)
    else:
        i=0
        r+=s[i]

    i+=1

# print(r,c)
x = c%7
if x==0:
    x = 7
print(x)