
def binarrySeach(a,x):
    left = 0
    right = len(a)
    while left<right:
        middle = (left+right)//2
        if a[middle]<= x:
            left = middle+1
        else:
            right = middle

    if left>0 and a[left-1]==x:
        return True
    else:
        return False



n,x,pos= list(map(int,input().split()))
a = [int(i) for i in range(1,n+1)]
for i in range(1,n+1):
    print(binarrySeach(a,x))




#
# from itertools import permutations
#
# n,x,pos= list(map(int,input().split()))
# comb = permutations(range(1,n+1), n)
#
# c = 0
# # Print the obtained combinations
# p = 0
# for i in list(comb):
#     l = list(i)
#     if l[pos-1]==x:
#         c+=1
# print(c)