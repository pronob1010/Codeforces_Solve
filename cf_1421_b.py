m=[]
for i in range(int(input())):
    n = int(input())
    for j in range(n):
        s=list(map(str, input().split()))
        sl= len(s)
        for i in range(sl):
            if j+1==i and s[j+1]=='1':
                print(s[j+1])
                m.append([j,i+1])

print(m)













# # function which return reverse of a string
#
# def isPalindrome(s):
# 	return s == s[::-1]
#
#
# s = input()
# ans = isPalindrome(s)
#
# if ans:
# 	print("0")
# else:
# 	print("No")


