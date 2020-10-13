for _ in range(int(input())):
    n = int(input())
    s = input()
    ss="abacaba"
    c=0
    ns=[]
    for i in range(1,len(s)+1):
        if s[i-1]== '?':
            if s[i-2]=='a':
                ns.append('d')
            else:
                ns.append(ss[c])
        else:
            ns.append(s[i-1])
        c += 1
        if c==len(ss):
            c=0




    fs =''.join([str(i) for i in ns])
    x = fs.count(ss)
    c1 = fs.find(ss)
    c2 = fs.rfind(ss)


    if x==1 and c1==c2:
        print("Yes")
        print(fs)
    else:
        print("No")
