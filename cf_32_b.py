s = input()
ms = []
i=1
while(i<=len(s)):
    if s[i-1] =='-' and s[i]=='.':
        ms.append('1')
        i+=2
    elif s[i-1] =='-' and s[i]=='-':
        ms.append('2')
        i += 2
    elif s[i-1] == '.':
        ms.append('0')
        i+=1

print(*ms,sep="")