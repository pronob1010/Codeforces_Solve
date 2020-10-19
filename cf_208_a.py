s = input()
l = len(s)
ns = []
i=2
temp=[]
while(i<=l+1):
    if s[i-2]=='W' and s[i-1]=='U' and s[i]=='B':
        i+=3
        temp.append(" ")
    else:
        temp.append(s[i-2])
        i+=1

nst = ''.join([str(i) for i in temp])
print(nst.strip())

