n=int(input())
a=list(map(int,input().split()))

b=[0]*3
# print(b)

for i in range(n):
	b[i%3]+=a[i]


m=max(b)
if b[0]==m:
	print("chest")
elif b[1]==m:
	print("biceps")
else:
	print("back")