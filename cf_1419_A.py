# t = int(input())
#
# for i in range(t):
#     ev = 0
#     odd = 0
#     n = int(input())
#     str = input()
#     for j in range(len(str)):
#         if int(str[j])%2 == 0:
#             if int(str[j]) == 0:
#                 continue
#             else:
#                 ev+=1
#         else:
#             odd +=1
#
#     if ev > odd:
#         print('2', end=" ")
#     elif ev < odd:
#         print('1', end=" ")

t = int(input())

for i in range(t):
    ev = 0
    odd = 0
    n = int(input())
    str = input()
    if len(str) is 1:
        if int(str[0])%2 == 0:
            print('2')
        else:
            print('1')
    elif len(str)%2 == 0:
        print('2')
    else:
        print('1')