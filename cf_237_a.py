d={}
for i in range(int(input())):
	s=input()
	d[s]=d.get(s,0)+1
# print(d)
print(max(d.values()))
