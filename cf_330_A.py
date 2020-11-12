n,m=map(int,input().split())
r=[]
c=[]
for i in range(n):
	x=input()
	for j in range(m):
		if x[j]=='S':
			r.append(i)
			c.append(j)

r=len(list(set(r)))
c=len(list(set(c)))
print(n*m-r*c)
