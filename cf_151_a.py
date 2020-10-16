n, k, l, c, d, p, nl, np = list(map(int, input().split()))
total_friend = n
total_drink = k*l
total_limes = c*d
total_salt = p

# print(total_friend,total_limes,total_drink,total_salt)
x = min((total_drink//nl),(total_limes//1),(total_salt//np))
# print(x)

print(x//total_friend)