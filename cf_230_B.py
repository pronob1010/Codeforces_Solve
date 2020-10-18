input()
s = list(map(int,input().split()))
for j in range(1,len(s)+1):
    c = 0
    n = s[j-1]//2
    for k in range(2,n+1):
        if s[j-1]%k==0:
            c+=1
    if c==1:
        print("YES")
    else:
        print("NO")