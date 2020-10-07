for i in range(5):
    s = list(map(int,input().split()))
    for j in range(5):
        if s[j] == 1:
            mrow = i+1
            mcol = j+1


move = abs(3-mrow)+abs(3-mcol)
print(move)