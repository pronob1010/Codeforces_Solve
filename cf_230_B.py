import math
input()
s = list(map(int,input().split()))
for j in range(1,len(s)+1):
    c = 0
    n = math.ceil(math.sqrt(s[j-1]))

    cn= math.ceil(math.sqrt(n))
    cf = 0
    for i in range(1,cn+1):
        if cn//i==0:
            cf=0
            break
        else:
            cf=1

    if cf == 1:
        for k in range(2,n+1):
            if ((s[j-1]%k==0) and (n*n==s[j-1])):
                if c<2:
                    c+=1
                else:
                    break
        if c==1:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")