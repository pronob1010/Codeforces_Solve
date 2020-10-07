# print(''.join('.'+x for x in input().lower() if x not in'aeyoui'))

s = input().lower()
vo = 'aeyoui'

for x in s:
    if x not in vo:
        print('.'+x,end="")
