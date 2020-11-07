import math
n, x, pos = map(int, input().split())
left= 0
right = n

more = n - x
less = n - more - 1
ans = 1
while left < right:
	mid = (left + right) // 2
	if mid < pos:
		ans *= less
		less -= 1
		left = mid + 1

	elif mid > pos:
		ans *= more
		more -= 1
		right = mid

	else:
		left = mid + 1

ans *= math.factorial(more + less)
print(ans % 1000000007)
