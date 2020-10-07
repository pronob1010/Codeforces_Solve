a= input()
b =input()
r = int(a)+int(b)
na =a.replace('0','')
nb =b.replace('0','')

r2 = int(na)+int(nb)
nr = str(r).replace('0','')
if int(r2) == int(nr):
    print("YES")
else:
    print("NO")
