n = input()
m = -1
for i in range(len(n)):
	if int(n[i])%2 == 0:
		m = i
		if n[i] < n[-1]:
			break
if m == -1:
	print(-1)
else:
	temp = list(n)
	temp[m] = n[-1]
	temp[-1] = n[m]
	print(''.join(temp))

# n = input()
# il = []
# m = -1
# f = 0
# ma = -1111
# for i in range(1,len(n)+1):
#     il.append(n[i-1])
#     if (int(n[i-1])%2==0) and (int(n[i-1])>=ma):
#         if int(n[i-1])>ma:
#             ma = int(n[i-1])
#             m = i-1
#
# print(m)
# if m == -1:
#     print(-1)
# else:
#     # print(il)
#     for i in range(1,len(il)+1):
#         r = il[len(il)-1]
#         if (int(il[i-1])%2==0) and (i-1) == int(m):
#             m = il[i-1]
#             print(r,m,i-1)
#             il[i-1] = il[i-1].replace(il[i-1], r)
#             il[len(il)-1]= il[len(il)-1].replace(il[len(il)-1], str(m))
#
#
#
#     print("\n")
#
#     # print(il)
#     for i in range(len(il)):
#         print(il[i],end="")
