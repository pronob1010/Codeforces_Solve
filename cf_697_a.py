a,b,c = list(map(int,input().split()))

p=a
r =a
i = 1

while True:
    if (c == p) or ( c == r):
        print("YES",i)
        break
    if r > c or p>c :
        print("No")
        break

    p = a + i * b
    r = a + i * b + 1
    i+=1

# def find(p,q,c):
#     if (c == p) or (c == r):
#         return 1
#     if r > c or p>c :
#         return 0
#     p = a + i * b
#     r = a + i * b + 1
#     find(p, q, c)
#     find(p, q, c)