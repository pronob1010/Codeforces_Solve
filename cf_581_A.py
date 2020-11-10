r, b  = list(map(int, input().split()))
day = min(r,b)
same = (max(r,b)-day)//2
print(day,same)