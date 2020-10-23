a , b = list(map(int,input().split()))
t = (a+1)//2
if b<=t:
    print(2*b-1)
else:
    print((b-t)*2)

#
# odd = []
# eve = []
# r = []
# for i in range(1,a+1):
#     if i%2==0:
#         eve.append(i)
#     else:
#         odd.append(i)
#
# r = odd+eve
# print(r)
# # print(r[b-1])