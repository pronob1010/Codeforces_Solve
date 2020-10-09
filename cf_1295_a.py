t = int(input())
for i in range(t):
    n = int(input())
    if n%2 == 1:
        print("7", end="")
        n=n-3

    if n%2==0:
        for i in range(n//2):
            print("1", end="")

    print("\n")

