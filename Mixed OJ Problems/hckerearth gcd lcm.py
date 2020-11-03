
def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)

for i in range(int(input())):
    a, b = list(map(int,input().split()))
    x = gcd(a,b)
    print(f"gcd {x}\nlcm {(a*b)//x}")