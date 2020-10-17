for i in range(int(input())):
    n = int(input())
    s = input()
    r =0
    j=2
    while(j<len(s)+1):
        if s[j-2]=='<' and s[j-1]=='>':
            r +=0


        elif s[j-2]=='>' and s[j-1]=='<':
            r +=1

        elif s[j-2]=='<' and s[j-1]=='<':
            r +=1

        elif s[j-2]=='>' and s[j-1]=='>':
            r +=1

        else:
            r +=1

        j+=1

    print(r)