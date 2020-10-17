for i in range(int(input())):
    s = input()
    l = len(s)
    for i in range(l):
        s=s.replace("AB","")
        s=s.replace("BB","")
    print(len(s))