k=int(input())
l=int(input())

i=0

while k**i<l:
	i+=1

if l==k**i:
	print("YES")
	print(i-1)
else:
	print('NO')