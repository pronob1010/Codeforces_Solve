a,b, c = list(map(int, input().split()))

r = (((a*(a+1))//2)*((b*(b+1))//2)*((c*(c+1))//2))

print(r%998244353)

# a = (a%998244353)
# b = (b%998244353)
# c = (c%998244353)
# r = 0
# print(a,b,c)
# for i in range(1,a+1):
#     for j in range(1,b+1):
#         for k in range(1,c+1):
#             r += (i*j*k)
# # print(b%998244353)
# # r = ((a%998244353) + (b%998244353)+ (c%998244353))%998244353
# print(r)

