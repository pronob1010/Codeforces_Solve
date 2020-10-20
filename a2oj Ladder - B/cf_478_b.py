n, m = list(map(int, input().split()))
t = n-(m-1)
max = (t*(t-1))//2


min = 0
t = n//m
# print(t)
pendding = n%m

t1=((int(t) + 1)*((int(t) + 1)-1))//2*pendding
t2=((t*(t-1))//2)*(m-pendding)

min= t1+t2



# for t in t1:
#     min+=(t*(t-1))//2
#

# print(min)
# if n%m==0:
#     min = min
# else:
#     min +=
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