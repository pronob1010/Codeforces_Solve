def isVal(arr, x, y, pos):
    for i in range(9):
        if arr[i][y] == pos:
            return False
    for j in range(9):
        if arr[x][j] == pos:

            return False

    sub_top_i= 3*(x//3)
    sub_top_j = 3*(y//3)

    for i in range(3):
        for j in range(3):
            if arr[sub_top_i+i][sub_top_j+j] == pos:

                return False
    return True

def solveSudoku(arr, i, j):
    if i == len(arr):
        print("true")
    else:
        next_i = 0
        next_j = 0

        if j == len(arr)-1:
            next_i = i+1
            next_j = 0
        else:
            next_i = i
            next_j = j+1


        if arr[i][j] != 0:
            solveSudoku(arr, next_i, next_j)
        else:
            for pos in range(1, 10):
                if isVal(arr, i, j , pos):
                    arr[i][j] = pos
                    solveSudoku(arr,next_i, next_j)
                    arr[i][j] = 0


def f_check(arr, x, y , pos):
    c = 0
    for j in range(len(arr)):
        if arr[x][j] == pos:
            c+=1
    if c>1:
        return False
    c1 = 0
    for i in range(len(arr)):
        if arr[i][y] == pos:
            c1 += 1
    if c1 > 1:
        return False
    c2 = 0
    sub_l_top_i = 3 * (x // 3)
    sub_l_top_j = 3 * (y // 3)
    for i in range(3):
        for j in range(3):
            if arr[sub_l_top_i + i][sub_l_top_j + j] == pos:
                c2 += 1
    if c2 > 1:
        return False
    else:
        return True

def is_valid(arr):
    f = 0
    c = 0
    for i in range(9):
        for j in range(9):
            if arr[i][j] != 0:
                if f_check(arr, i, j , arr[i][j]):
                    c+=1
                    f = 1
                else:
                    # print(arr[i][j])
                    f = 0
                    break
        if f == 0:
            break
    # print(f)
    if f == 1:
        return True
    else:
        return False

arr = []
for i in range(9):
    s = list(map(int, input().split()))[:9]
    arr.append(s)
if is_valid(arr):
    solveSudoku(arr, 0, 0)
else:
    print("false")
