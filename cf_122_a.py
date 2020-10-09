n = int(input())
f = 0
ln = [4,7,44,47,74,77,444,447,474,477,744,747,774,777]
for i in ln:
    if (n%i == 0 ):
        f = 1
        break

if (f == 1):
    print("YES")
else:
    print("NO")