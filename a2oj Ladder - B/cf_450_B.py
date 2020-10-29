n = int(input())
h = 0
res = 0
for i in range(n):
    print("check ",res)
    s = int(input())
    res+= abs(s-h) + 1

    if i!= 0:
        res+=1
    h=s

print(res)
