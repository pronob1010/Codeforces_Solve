# target =float(str((a//b))+".50")
        # res = a/b
        # if (target>res):
        #     print(math.floor(res+1))
        # else:
        #     print(math.ceil(res+1))

t = int(input())
for i in range(t):
    res = 2
    c =1
    a,b = list(map(int,input().split()))
    if a == 1:
        print("1")
    else:
        for j in range(2,a,b):
            res+=b
            c +=1

        print(c)
        c = 0

# testcase = int(input())
# for i in range(testcase):
#     count=0
#     n,k = list(map(int,input().split()))
#     rem =0
#     if n>0:
#         count+=1
#         n=n-2
#     if n<k and n>0:
#         count+=1
#     else:
#         rem = n%k
#         d = int((n-rem)/k)
#         count+= d
#         if rem!=0:
#             count+=1
#     print(count)
