import math
s1, s2, s3 = list(map(int, input().split()))
v2 = s1*s2*s3
print(int(4 * (math.sqrt(v2 / (s1 * s1)) + math.sqrt(v2 / (s2 * s2)) + math.sqrt(v2 / (s3 * s3)))))
