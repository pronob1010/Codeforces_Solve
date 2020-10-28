import math
for i in range(int(input())):
    n = int(input())
    st = input()
    l = len(st)
    s1 = []
    s2 = []
    s3 = []
    m = 1
    c = 0
    for j in range(2,l+1):
        if st[j-2] == st[j-1]:
            c += 1
    print(math.ceil(c/2))


