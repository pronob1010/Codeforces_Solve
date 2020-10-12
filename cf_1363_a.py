for i in range(int(input())):
    n,r = list(map(int, input().split()))
    s = list(map(int, input().split()))[:n]
    result = 0
    if len(s)>1:
        even = []
        odd = []
        for j in s:
            if j%2 == 0:
                even.append(j)
            else:
                odd.append(j)

        result = odd[0]
        r-=1
        if r%2 == 0 and len(odd)-1>0:
            for j in range(2,r):
                result += odd[j-1]+odd[j]
                r -= 2
                j+=1
        elif r%2==1 and len(odd)-1>0 :
            for j in range(1,r-1):
                result += odd[j-1]+odd[j]
                j+=1
                r -= 2
        for k in range(1,r):
            result+=even[k-1]
    else:
        result += s[0]



    if result%2==1:
        print("Yes")
    else:
        print("No")


