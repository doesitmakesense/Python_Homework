a = 3
b = 2
c = 4
'''
if c % 2 == 1:
    if c == a or c == b:
        print('yes')
    else:
        print('no')

if c % 2 == 0:
    if a * b > c:
        if c >= a or c >= b:
            print('yes')
        elif a % 2 == 0 and b % 2 == 0 and c % 2 == 0:
            print('yes')
        else:
            print('no')
    else:
        print('no')
'''

if c <= b * a and (c % a == 0 or c % b == 0):
    print('yes')
else:
    print('no')