n ,s , t= list(map(int, input().split()))
p = list(map(int,input().split()))

for i in range(n):
    if s == t:
        print(i)
        break
    s = p[s-1]
else:
    print(-1)