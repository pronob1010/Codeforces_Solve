import math
r,x,y,x1,y1 = list(map(int, input().split()))

ans = math.ceil(math.sqrt((x-x1)*(x-x1)+(y-y1)*(y-y1))/(2*r))
print(ans)
