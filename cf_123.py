# def Fibonacci(n):
# 	if n==1:
# 		return 0
# 	elif n==2:
# 		return 1
# 	else:
# 		return Fibonacci(n-1)+Fibonacci(n-2)
# ------------------------------
# def Fibonacci(n):
#    if n <= 1:
#        return n
#    else:
#        return(Fibonacci(n-1) + Fibonacci(n-2))

# def Fibonacci(n):
#     # Taking 1st two fibonacci nubers as 0 and 1
#     FibArray = [0, 1]
#
#     while len(FibArray) < n + 1:
#         FibArray.append(0)
#
#     if n <= 1:
#         return n
#     else:
#         if FibArray[n - 1] == 0:
#             FibArray[n - 1] = Fibonacci(n - 1)
#
#         if FibArray[n - 2] == 0:
#             FibArray[n - 2] = Fibonacci(n - 2)
#
#     FibArray[n] = FibArray[n - 2] + FibArray[n - 1]
#     return FibArray[n]


def Fibonacci(n):
    a = 0
    b = 1
    if n == 0:
        return a
    elif n == 1:
        return b
    else:
        for i in range(2,n+1):
            c = a + b
            a = b
            b = c
        return b
n = int(input())
sum = 0

for i in range(1,n+1):
  sum +=Fibonacci(i)
print(sum)


