input()
s = list(map(int, input().split()))

m = sorted(s)

for i in range(1,len(s)+1):
    j = 0
    while(True):
        if m[i-1]==s[j]:
            print(j+1,end=" ")
            break
        j+=1