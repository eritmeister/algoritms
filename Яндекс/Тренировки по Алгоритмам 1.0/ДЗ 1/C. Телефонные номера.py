def format_number(number):
    digits = set('0123456789')
    result = ''
    for s in number:
        if s in digits:
            result += s
    if len(result) == 7:
        result = '495' + result
    return result[-10:]


correct = format_number(input())
for _ in range(3):
    if correct == format_number(input()):
        print('YES')
    else:
        print('NO')
