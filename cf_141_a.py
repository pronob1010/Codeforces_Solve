# n2={}
# t= "NewYearandChristmasMen"
# t=t.upper()
# for i in range(1,len(t)+1):
#     if t[i-1] in n2:
#         n2[t[i-1]]+=1
#     else:
#         n2[t[i-1]] = 1
# n2 = sorted(n2)
# print(n2)



s=[]
x = input()
y = input()
z = input()
# print(len(x), len(y), len(z))
new = x+y
new = sorted(new)
z= sorted(z)
# print(z)
# print(new)
# xl = len(z)-len(new)
# print(xl)
if new==z:
    print("YES")
else:
    print("NO")


# s = ''.join(a)

# print(s)
#
# for i in range(1,len(s)+1):
#     if s[i-1] in n:
#         n[s[i-1]]+=1
#     else:
#         n[s[i-1]] = 1
# n = sorted(n)
# print(n)

# final = {}
#
# for key in n2:
#     if key in n and n2.get(key)<= n.get(key):
#         final[key] = n2[key]
#     else:
#         break
#
# print(final)
#
# is_equal = n == n2
# print(is_equal)
