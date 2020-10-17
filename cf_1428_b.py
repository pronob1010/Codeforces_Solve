for i in range(int(input())):
    n = int(input())
    s = input()
    r =0
    j=1
    while(j<len(s)+1):
        if s[j-1]=='<' and s[j]=='>':
            r +=0
            j+=2
        elif s[j-1]=='>' and s[j]=='<':
            r +=1
            j += 2
        else:
            r +=1
            j+=1
    print(r)