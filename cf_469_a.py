t = int(input())
s1=list(map(int,input().split()))
s2=list(map(int,input().split()))

# p = set(s1)|set(s2)
# print(p)
nl = []
for i in range(len(s1)-1):
    if s1[i]!=0:
        nl.append(s1[i])
for i in range(len(s2)-1):
    if s2[i] not in nl and s2[i]!=0:
        nl.append(s2[i])

# print(set(nl))
if len(set(nl))!=t:
    print("Oh, my keyboard!")
else:
    print("I become the guy.")

# n=int(input())
# b,*p=map(int,input().split())
# d,*q=map(int,input().split())
# c=set(p)|set(q)
# if len(c)==n:
# 	print("I become the guy.")
# else:
# 	print("Oh, my keyboard!")