# def twoPointer(li,x):
#     l = 0
#     r = len(li)-1
#     s = sum(li[l:r])
#     while(l<=r):
#         if s == x:
#             return True
#         elif sum(li[l:r])<x:
#             l+=1
#         elif sum(li[l:r])>x:
#             r-=1
#     else:
#         return False

t = int(input())
for i in range(t):

    n = int(input())
    p = list(map(int,input().split()))
    # ans = False
    # s = []
    # for i in range(n):
    #      if s[p[i]]:
    #          ans = True
    #          break
    #      s[p[i]]+=1
    # print(s)
    # f = {}
    # for j in p:
    #     if j in f:
    #         f[j]+=1
    #     else:
    #         f[j]=1
    # print(f)

    if len(set(p))<len(p):
        print("YES")
    else:
        print("NO")