s = input().lower()
# s1= set(s)
s1 = []
s2 = ['h','e','l','l','o']
j=1
ls2= len(s2)
for i in range(len(s)):
    if (j <= ls2):
        if (s[i] == s2[j - 1]):
            # print(s[i], i, j)
            j += 1
    else:
        break

if j-1 == ls2:
    print("YES")
else:
    print("NO")
    # xqjqmenkodmlhzyzmmvofdngktygbbxbzpluzcohohmalkoeuwfikblltaaigv