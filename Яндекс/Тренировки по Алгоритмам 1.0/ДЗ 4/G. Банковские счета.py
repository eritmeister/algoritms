users = dict()
with open('input.txt') as f:
    for line in f:
        words = line.split()
        if words[0] == 'DEPOSIT':
            if words[1] not in users:
                users[words[1]] = 0
            users[words[1]] += int(words[2])
        elif words[0] == 'WITHDRAW':
            if words[1] not in users:
                users[words[1]] = 0
            users[words[1]] -= int(words[2])
        elif words[0] == 'BALANCE':
            if words[1] not in users:
                print('ERROR')
            else:
                print(users[words[1]])
        elif words[0] == 'TRANSFER':
            if words[1] not in users:
                users[words[1]] = 0
            users[words[1]] -= int(words[3])
            if words[2] not in users:
                users[words[2]] = 0
            users[words[2]] += int(words[3])
        elif words[0] == 'INCOME':
            for user in users.keys():
                if users[user] > 0:
                    users[user] = int(users[user] * (100 + int(words[1])) / 100)
