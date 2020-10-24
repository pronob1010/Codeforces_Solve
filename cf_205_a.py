n = int(input())
s = list(map(int, input().split()))
x = min(s)
x2 = s.count(x)

if x2>1:
    print("Still Rozdil")
else:
    print(s.index(x) + 1)
