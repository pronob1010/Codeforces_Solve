s1 = input()
s2 = input()

for i in range(1,len(s1)+1):
    if s1[i-1]==s2[i-1]:
        print("0", end="")
    else:
        print("1", end="")