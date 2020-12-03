k = int(input())
l = int(input())


# print(l%k)
p = int(l/k)


if l%k == 0:
    if k!=l:
        i = 2
        while True:
            if 2*(k ** (i)) == l :
                print("YES")
                r = i
                break
            if (k ** (i)) == l:
                print("YES")
                r = i
                break
            else:
                i+=1

        if k**r == l or 2*(k**r)==l:
            print(r)
        elif k**(r-1) == l or 2*(k**(r-1)) == l:
            print(r-1)
    else:
        print("YES")
        print(0)

else:
    print("NO")
