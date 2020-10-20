n, m = list(map(int, input().split()))

t = n-(m-1)
max = (t*(t-1))//2

t = n//m
r1 = (t*(t-1))//2
min=r1*m

if n%m==0:
    min = min
else:
    min +=n%m
print(min,max)


# n, m = list(map(int, input().split()))
# t = n//m
#
# r = (t*(t-1))//2
# print(r,r)

# if m==1:
#     t = n
#     r = (t*(t-1))//2
#     print(r,r)
# else: