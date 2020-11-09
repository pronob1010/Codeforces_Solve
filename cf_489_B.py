def twoPoint(g,i,x,c,used):
    start = i
    end = len(g)-1
    while(start<=end):
        # print(x)
        if abs(g[start]-x)<=1:
            c+=1
            g[start]=-100
            break
        start += 1

    return c



n = int(input())
b = list(map(int, input().split()))
m = int(input())
g = list(map(int, input().split()))

b.sort()
g.sort()

used = []
c = 0
r = 0
for i in range(len(b)):
    r += twoPoint(g,0,b[i],c,used)

print(r)
# print(g)