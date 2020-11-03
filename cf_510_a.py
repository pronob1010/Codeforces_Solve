a, b = list(map(int, input().split()))

for i in range(b):
    print("#",end="")
print()
f = 1
for i in range(a-2):
    if i%2==0:
        p = 0
        if f==0:
            f = 1
            p = 1
            print("#",end="")
        for j in range(b-1):
            print(".", end="")
        if f ==1 and p == 0:
            print("#", end="")
            f = 0
        print()
    else:
        for i in range(b):
            print("#", end="")
        print()
for i in range(b):
    print("#",end="")
