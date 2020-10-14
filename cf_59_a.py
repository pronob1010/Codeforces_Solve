st = input()
s = [str(st[i]) for i in range(len(st))]
x= len(s)
u=0
l=0
for i in range(1,x+1):
    if s[i-1]>='A' and s[i-1]<='Z':
        u+=1

    elif s[i-1]>='a' and s[i-1]<='z':
        l+=1

# print(u,l,x)
if u==(x):
    print(st.upper())
elif l==(x):
    print(st.lower())
elif u == l:
    print(st.lower())
else:
    print(st.lower())
