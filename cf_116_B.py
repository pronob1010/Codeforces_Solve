n, m = list(map(int, input().split()))
list1 = []
for i in range(n):
    s = list(input())
    list1.append(s)

print(list1)
print('------')
for i in range(n):
    for j in range(m):
        print(list1[i][j])
        print(list1[i][j+1])
        print(list1[i+1][j])
    print('------')