for i in range(int(input())):
    n = input()
    nl =len(n)
    fn = int(n[0])

    r = (10*(fn-1))+((nl*(nl+1))//2)

    print(r)