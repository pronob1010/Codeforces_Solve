
def fun(s):
    s1 = s
    while(s1>0):
        r = s1%10
        if(r != 0):
            if s%r != 0:
                return 0
        s1//=10
    return 1

t= int(input())
for i in range(t):
    s = int(input())
    while not fun(s):
        s+=1
    print(s)
