st = input()
s = [str(i) for i in st]

s1 = {}
for i in s:
    if i in s1:
        s1[i] += 1
    else:
        s1[i] = 1

v = [str(i) for i in s1.keys()]
c = 0
for i in v:
    if (i == 'A' or i == 'E' or i == 'O' or i == 'U'):
        c += 1

if c == 0:
    c = 2
print(c)

#
# frequencies = {}
# for item in a_list:
#     if item in frequencies:
#         frequencies[item] += 1
#     else:
#         frequencies[item] = 1