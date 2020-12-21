t= int(input())
for i in range(t):
    s = int(input())
    while True:
        s_copy = str(s)
        dig = []
        for i in range(len(s_copy)):
            if s_copy[i]!='0' and s_copy[i] not in dig:
                dig.append(int(s_copy[i]))
        c = 0
        for j in dig:
            if s%j==0:
                c+=1
        if len(dig)==c:
            print(s)
            break
        s+=1