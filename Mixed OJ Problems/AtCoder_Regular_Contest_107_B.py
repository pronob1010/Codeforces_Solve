n = 20
print(bin(n))
if (n & (1<<60)):
    print("YES")
else:
    print("NO")