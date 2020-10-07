a,b= list(map(int, input().split()))
p = 1
while True:
    r = a*p
    if r%10 == 0 or r%10 == b:
        print(p)
        break
    p+=1
