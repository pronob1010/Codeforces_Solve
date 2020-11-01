f = []

def fibo(n):
    a = 0
    b = 1
    if n==1:

        return b
    else:
        for i in range(2, n):
            c = a+b
            a = b
            b = c
        return b

for i in range(1,1001):
    f.append(fibo(i))

x = int(input())
for i in range(1,x+1):
    if i in f:
        print('O', end="")
    else:
        print('o', end="")