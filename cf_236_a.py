s = input()
f = 0
for i in range(len(s)):
    if s[i]=='a' and s[i]=='e' and s[i]=='i' and s[i]=='o' and s[i]=='u':
        f = 1
        break

if f == 0:
    print("IGNORE HIM!")
else:
    print("CHAT WITH HER!")