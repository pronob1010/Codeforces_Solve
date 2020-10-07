n = int(input())
s = list(map(int,input().split()))[:n]
s.sort()
print(*s, sep=" ")