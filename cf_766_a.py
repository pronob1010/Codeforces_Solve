if __name__== "__main__":
    s1 = input()
    s2 = input()

    if s1==s2:
        print(-1)
    else:
        print(max(len(s1), len(s2)))


# def tp(s2,x):
#     start = 0
#     c = 0
#     c1 = 0
#     end = len(s2)- 1
#     while (start <= end):
#         if s2[start]==x or s2[end]==x:
#             c+=1
#         else:
#             c1+=1
#         start+=1
#         end-=1
#     return c1
#
# if __name__== "__main__":
#     s1 = input()
#     s2 = input()
#     r = 0
#     for i in range(len(s1)):
#         x = s1[i]
#         r += tp(s2,x)
#
#     print(r)