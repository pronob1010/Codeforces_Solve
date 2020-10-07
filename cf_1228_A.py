def repeated_digit(n):
    a = []
    # Traversing through each digit
    while n != 0:
        d = n % 10
        # if the digit is present more than once in the number
        if d in a:
            # return 0 if the number has repeated digit
            return 0
        a.append(d)
        n = n // 10
    # return 1 if the number has no repeated digit
    return 1

l=[]
a,b = list(map(int, input().split()))
for i in range(a,b+1):
    n=i
    if repeated_digit(n) is 1:
        l.append(i)

if len(l) > 0:
    print(l[0])
else:
    print('-1')

