n = int(input())
s = list(map(int, input().split()))[:n]

m = 1001
d = abs(s[0] - s[n-1])
m = min(d,m)
idx1 =1
idx2 =n
for i in range(1,n):
    d = abs(s[i-1]-s[i])
    if m>d:
        m = d
        idx1 = (i-1)+1
        idx2 = i+1
print(idx1, idx2)

# dic = sorted(([v, i] for i, v in enumerate(s)))
# print(dic[0][1]+1, dic[1][1]+1)

# a=[]
# for i in range(n):
#     a.insert(s[i],i)
#
# print(a)
#
# print ("The original list is : " + str(s))
#
# res = [((i), s[i]) for i in range(len(s))]
#

# # printing result
# print ("The pair list is : " + str(res))

