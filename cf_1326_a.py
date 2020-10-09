t = int(input())
for j in range(t):
    n = int(input())
    if n > 0 and n != 1:
        print("2", end="")
        for i in range(1, n):
            print("3", end="")

    else:
        print("-1")
    print("\n")
