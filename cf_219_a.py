n=int(input())
s=sorted(input())
# print(s)
x=s[::n]*n
# print(x)
if sorted(x)==s:
    print("".join(x))
else:
    print(-1)





# n = int(input())
# s = input()
# p = {}
# for i in range(1,len(s)+1):
#     if s[i-1] in p:
#         p[s[i-1]]+=1
#     else:
#         p[s[i-1]] = 1
#
# # print(p)
# f=0
# for i in p.values():
#     if n==i:
#         f=1
#     else:
#         f=0
#         break
#
# if f == 1:
#     k = len(p.keys())
#     # print(k)
#     klist = [str(i) for i in p.keys()]
#     # print(klist)
#
#     for i in range(n):
#         print(*klist, sep="",end="")
#
#
# else:
#     print("-1")