n = input()
f= 0
c = 0
t = int(n)

while(t!=0):
    if t%10==4 or t%10 == 7:
        f =1
        c+=1
    t//=10

if c ==4 or c==7:
    print("YES")
else:
    print("NO")

# n = input()
# f = 0
# t = int(n)
# if len(n)!=1:
#     while(t!=0):
#         if t%10==4 or t%10 == 7:
#             f =1
#         else:
#             f =0
#             break
#         t//=10
# else:
#     if int(n[0])==7:
#         f = 0
#
# if f ==1:
#     print("YES")
# else:
#     print("NO")
