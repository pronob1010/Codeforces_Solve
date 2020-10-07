a_list = []
n = int(input())
st = input()

for i in range(n):
    a_list.append(st[i])

#frequencie counting
frequencies = {}
for item in a_list:
    if item in frequencies:
        frequencies[item] += 1
    else:
        frequencies[item] = 1

o_count = 0
n_count = 0
e_count = 0

o_count = frequencies.get('o')
n_count = frequencies.get('n')
e_count = frequencies.get('e')

try:
    r = min(o_count,n_count,e_count)

    u_o = (frequencies.get('o') - r)
    u_n = (frequencies.get('n') - r)
    u_e = (frequencies.get('e') - r)

    frequencies.update({'o': u_o})
    frequencies.update({'n': u_n})
    frequencies.update({'e': u_e})

    for _ in range(r):
        print('1 ',end ="")
except:
    pass


z_count = frequencies.get('z')
e_count = frequencies.get('e')
r_count = frequencies.get('r')
o_count = frequencies.get('o')

try:
    s = min(z_count,e_count,r_count,o_count)

    for _ in range(s):
        print('0 ',end ="")
except:
    pass
