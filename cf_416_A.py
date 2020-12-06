n = int(input())
s = []

# condition = []
# number = []
# YesNo = []
# f = 0
# f2 = 0

for i in range(n):
    x = list(map(str, input().split(" ")))
    s.append(x)
print(s)

r = 0
for i in range(len(s)):
    condition = s[i][0]
    number = int(s[i][1])
    YesNo = s[i][2]


    if condition == '>' or condition == '>=':
        if YesNo == 'Y':
            if r > number:
                r = r
            else:
                r += (number + 1)

        elif YesNo == 'N':
            if r > number:
                r = r
            else:
                r -= number


    elif condition == '<' or condition == "<=":
        if YesNo == 'Y':
            if r < number:
                r = r
            else:
                r += number
        elif YesNo == 'N':
            if r < number:
                r += number
            else:
                r = r

    print(r)

print(r)



