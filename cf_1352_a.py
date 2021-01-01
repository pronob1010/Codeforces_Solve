# t = int(input())
# for i in range(t):
#     s = input()
#     l = len(s)
#     ro = []
#     mro = []
#     for j in range(l,0,-1):
#         if(int(s[j-1])>0):
#             st = s[j-1]
#             if (l-(j)) > 0:
#                 st+='0'*(l-(j))
#             ro.append(st)
#     print(len(ro))
#     print(*ro, sep=" ")


t = int(input())
for i in range(t):
    n = input()
    ll = len(n)
    n = int(n)
    round_Number_List = []
    x = 10
    for j in range(ll):
        last_digit = n%x
        if last_digit!= 0:
            round_Number_List.append(last_digit)
        x*=10
        n-=last_digit
    print(len(round_Number_List))
    print(*round_Number_List, end=" ")


