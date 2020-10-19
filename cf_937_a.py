n = int(input())
s = list(map(int,input().split()))
ns = [int(i) for i in s if i>0]
print(len(set(ns)))