n = int(input())
array = []
for i in range(n-1 ,0,-1):
    array.append(i)
# print(array)
# for i in range(1,len(array)-1):
#     array[i],array[i+1] = array[i+1],array[i]
array.sort()
print(n, end=" ")
print(*array,sep=" ")