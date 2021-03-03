n, m = list(map(int, input().split()))
list1 = []
for i in range(n):
    s = list(input())
    list1.append(s)

print(list1)
print('------')
for i in range(1,n):
    for j in range(1,m):
        print(list1[i-1][j-1])
        print(list1[i-1][j])
        print(list1[i][j-1])
        print('------')