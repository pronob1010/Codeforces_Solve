a, b = list(map(int,input().split()))
ch = []
for i in range(a):
    c = list(map(str,input().split()))[:b]
    for i in c:
        if i == 'W' or i == 'G' or i == 'B':
            ch.append(i)

if len(ch) == a*b:
    print("#Black&White")
else:
    print("#Color")
