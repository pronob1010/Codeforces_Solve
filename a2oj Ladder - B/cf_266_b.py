a,b = list(map(int,input().split()))
s = input()[:a]
for i in range(b):
    s = s.replace("BG","GB")
print(s)

