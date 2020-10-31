# def isValid(arr, x , y , posibleValue):
#     for j in range(9):
#         if arr[x][j] == posibleValue:
#             return False
#     for i in range(9):
#         if arr[i][y] == posibleValue:
#             return False
#     sub_top_left_i = 3*(x//3)
#     sub_top_left_j = 3*(y//3)
#     for i in range(3):
#         for j in range(3):
#             if arr[sub_top_left_i+i][sub_top_left_j+j]==posibleValue:
#                 return False
#     return True
#
# def solveSuduko(arr, i, j):
#     if i== len(arr):
#         return arr
#     else:
#         next_i =0
#         next_j =0
#
#         if j==len(arr)-1:
#             next_i = i+1
#         else:
#             next_i = i
#             next_j = j+1
#
#         if arr[i][j] != '0':
#             solveSuduko(arr, next_i, next_j)
#         else:
#             for posibleValue in range(1,10):
#                 if isValid(arr, i , j , posibleValue):
#                     arr[i][j] = posibleValue
#                     solveSuduko(arr, next_i, next_j)
#                     arr[i][j] = 0
#
#
#
# for i in range(int(input())):
#     arr = []
#     for j in range(9):
#         p = input()
#         s = []
#         for k in range(len(p)):
#             s.append(p[k])
#         arr.append(s)
#
# solveSuduko(arr, 0, 0)
# for i in arr:
#     print(*i, sep="")

for i in range(int(input())):
    arr = []
    for j in range(9):
        p = input()
        p = p.replace('1','2')

        print(p)

