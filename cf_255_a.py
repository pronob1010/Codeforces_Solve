L = [0, 0, 0]

L1 = ["chest", "biceps", "back"]

input()

for k, j in enumerate(map(int, input().split(" "))):
    L[k % 3] += j

print(L1[L.index(max(L))])