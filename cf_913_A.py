n = int(input())
m = int(input())
# print((1<<n))
r = m%(1<<n)


# p = (2 ** (n // 2))
# p = p * p
#
# if n%2==1:
#     p*=2
#
# r = m%(p)
print(r)