s = list(map(int,input().split()))
r = sum(s)

if (r != 0) and (r%5==0):
    print(r//5)
else:
    print('-1')