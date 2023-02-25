a = int(input())
b = int(input())
c = int(input())
if c < 0:
    print('NO SOLUTION')
elif c ** 2 - b == 0:
    if a == 0:
        print('MANY SOLUTIONS')
    else:
        print(0)
elif a == 0:
    print('NO SOLUTION')
elif (c ** 2 - b) % a == 0:
    print((c ** 2 - b) // a)
else:
    print('NO SOLUTION')
