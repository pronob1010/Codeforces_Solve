t = int(input())
t+=1
while True:
    y = []
    n = t
    while(n!=0):
        if n%10 not in y:
            y.append(n%10)
        else:
            break
        n//=10
    t1 = str(t)
    if len(y) == len(t1):
        print(t)
        break
    t+=1

#
# t = 2013
# y = []
# n = t
# while(n!=0):
#     if n%10 not in y:
#         y.append(n%10)
#     else:
#         break
#     n//=10
#
# print(len(y))
