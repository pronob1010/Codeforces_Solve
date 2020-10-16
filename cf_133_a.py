s = input()

for i in range(1,len(s)+1):
    if s[i-1] == 'H' or s[i-1] == 'Q' or s[i-1]== '9':
        print("YES")
        break
else:
    print("NO")