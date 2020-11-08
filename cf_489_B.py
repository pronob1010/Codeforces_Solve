def twoPoint(g,i,x,c,used):
    start = i
    end = len(g)-1
    while(start<=end):
        # print(x)
        if abs(g[start]-x)==1 and g[start] not in used:
            c+=1
            used.append(g[start])
        else:
            start += 1
    else:
        return c



n = int(input())
b = list(map(int, input().split()))
m = int(input())
g = list(map(int, input().split()))

b.sort()
g.sort()
print(b)
print(g)
used = []
c = 0
for i in range(len(b)):
    twoPoint(g,0,b[i],c,used)

print(len(used))