list = [9, 99 , 999, 9999, 99999, 999999, 9999999, 99999999, 999999999]
n = int(input())
c = 0
for i in list:
    if n>i:
        c+=1
    else:
        break
r = 0
for i in range(c+1):
    # print(i)
    if n>list[i]:
        n-=list[i]
        r +=list[i]
    else:
        r += (i+1)*n
    # print(n,r)
print(r)