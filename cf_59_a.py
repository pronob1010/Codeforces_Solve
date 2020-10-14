st = input()
s = [str(st[i]) for i in range(len(st))]
x= len(s)
u=0
l=0
for i in range(1,x):
    if s[i-1]>='A' and s[i]<='Z':
        u+=1
    else:
        l+=1

if u==l:
    print(st.upper())
else:
    print(st.lower())
