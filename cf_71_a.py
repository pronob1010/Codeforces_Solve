t = int(input())
for i in range(t):
    s = input()
    if len(s)<=10:
        print(s)
    else:
        print(s[0], end="")
        print(len(s)-2, end="")
        print(s[len(s)-1])
    print("\n")
