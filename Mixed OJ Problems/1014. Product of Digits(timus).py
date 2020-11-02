n = int(input())
s =''

if n%2==0:
    x = n//2
    y = 2
    s +=str(y)
    s += str(x)
else:
    x = n
    y = 1
    s += str(x)
    s += str(y)

print(s)