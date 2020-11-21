# t = int(input())
# for j in range(t):
#     n , q = list(map(int, input().split()))
#     s = input()
#     mf = {}
#     for k in range(len(s)):
#         if s[k] in mf:
#             mf[s[k]] += 1
#         else:
#             mf[s[k]] = 1
#     for l in range(q):
#         p,m = list(map(int, input().split()))
#         ns = s[p-1:m]
#         f2 = {}
#         for k in range(len(ns)):
#             if ns[k] in f2:
#                 f2[ns[k]] += 1
#             else:
#                 f2[ns[k]] = 1
#         l1 = list(mf.values())
#         l2 = list(f2.values())
#         print(l1,l2)
#         if l1>l2:
#             print("YES")
#         else:
#             print("NO")
#

t = int(input())
for j in range(t):
    n , q = list(map(int, input().split()))
    s = input()
    mf = {}
    for l in range(q):
        p,m = list(map(int, input().split()))
        p-=1
        m-=1
        x = 0
        y = len(s)-1
        r = False
        while True:
            if (x>=p and y<=m):
                break

            if (s[x]==s[p] and x<p):
                r = True
                break

            elif (s[y] == s[m] and y>m):
                r = True
                break
            x+=1
            y-=1
        if r and m-p+1>=2:
            print("YES")
        else:
            print("NO")
