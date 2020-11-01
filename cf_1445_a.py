t = int(input())
for i in range(t):
    n , x= list(map(int, input().split()))
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    if i!=t-1:
        input()
    a.sort()
    b.sort(reverse=True)
    # print(a)
    # print(b)
    c = 0
    for j in range(n):
        # print(a[j]+b[j])
        if a[j]+b[j]<=x:
            c+=1
    if c == n:
        print("Yes")
    else:
        print("No")