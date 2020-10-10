n,m,a = map(int,input().split())
s = m//a
k = n//a
if m%a != 0:
	s+=1
if n%a !=0:
	k+=1
g=s*k
print(g)