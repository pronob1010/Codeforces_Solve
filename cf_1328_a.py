for i in range(int(input())):
    a,b = list(map(int,input().split()))
    r = b-a
    print(r%b)

# for i in range(int(input())):
#     a,b = list(map(int,input().split()))
#     m=0
#     while True:
#         if a%b==0:
#             print(m)
#             break
#         else:
#             a+=1
#             m+=1
