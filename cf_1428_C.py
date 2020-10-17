for i in range(int(input())):
    s = input()
    l = len(s)
    for i in range(l):
        # s = s.replace("AB", "")
        # s = s.replace("BB", "")

        if l%2==0:
            s = s.replace("AB", "")
            l-=2

        else:
            s = s.replace("BB", "")
            l-=2

    # if l % 2 == 1:
    #     s = s.replace("BB", "")
    #
    #
    # else:
    #
    #     s = s.replace("AB", "")


    print(len(s))