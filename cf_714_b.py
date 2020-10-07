n=input()
s = set(map(int,input().split()))
if len(s)>3:
  print ('NO')
elif len(s)<=2:
  print ('YES')
else:
  l = sorted(list(s))
  mid = 3//2
  if abs(l[0]-l[mid]) == abs(l[2]-l[mid]):
      print("YES")
  else:
      print("NO")