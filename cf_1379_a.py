t = int(input())
for i in range(t):
	l = int(input())
	s = input()
	if 'abacaba' in s:
		if 'abacaba' in s[s.index('abacaba') + 1:]:
			print('NO')
		else:
			print('YES')
			print(s.replace('?', 'z'))
	else:
		for i in range(l - 6):
			p = True
			for a, b in zip(s[i:i+7], 'abacaba'):
				if not a in [b, '?']:
					p = False
					break
			if p:
				r = s.replace('?', 'z')
				r = r[:i] + 'abacaba' + r[i+7:]
				if 'abacaba' in r and not 'abacaba' in r[r.index('abacaba') + 1:]:
					print('YES')
					print(r)
					break
				else:
					p = False
		if not p:
			print('NO')

# for _ in range(int(input())):
#     n = int(input())
#     s = input()
#     ss="abacaba"
#     c=0
#     ns=[]
#     for i in range(1,len(s)+1):
#         if s[i-1]== '?':
#             if s[i-2]=='a':
#                 ns.append('d')
#             else:
#                 ns.append(ss[c])
#         else:
#             ns.append(s[i-1])
#         c += 1
#         if c==len(ss):
#             c=0
#
#
#
#
#     fs =''.join([str(i) for i in ns])
#     x = fs.count(ss)
#     c1 = fs.find(ss)
#     c2 = fs.rfind(ss)
#
#
#     if x==1 and c1==c2:
#         print("Yes")
#         print(fs)
#     else:
#         print("No")
