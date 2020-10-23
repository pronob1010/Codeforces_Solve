s = input()
# print(s)
p = []
for i in range(1,len(s)+1):

    if not(s[i-1] == '{' or s[i-1]==',' or s[i-1]==' ' or s[i-1]=='}'):
        p.append(s[i-1])

x = len(set(p))
print(x)