s = input()

seq = {}
for i in s:
    if i in seq:
        seq[i] += 1
    else:
        seq[i] = 1

if len(seq)%2 == 1:
    print("IGNORE HIM!")
else:
    print("CHAT WITH HER!")