n = input()
f = 0
t = int(n)
while(t!=0):
    if t%10==4 or t%10 == 7:
        f =1
    else:
        f =0
        break
    t//=10

if f ==1:
    print("YES")
else:
    print("NO")
