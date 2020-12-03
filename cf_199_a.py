def fibonacci(n):
    flist = []
    a = 0
    b = 1
    flist.append(a)
    flist.append(b)

    for i in range(2,n):
        c = a + b
        a = b
        b = c
        if b<n:
            flist.append(b)
        else:
            flist.append(b)
            break
    return flist

n = int(input())
li = fibonacci(n)
