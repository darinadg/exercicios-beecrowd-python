a = input()
b = input()

if a == 'V':
    if b == 'V':
        print('VV')
    else:
        print('?')
elif a == 'F':
    if b == 'F':
        print('FF')
    else:
        print('?')
else:
    print('?')

