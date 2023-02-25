d = dict()
with open('input.txt') as f:
    for line in f:
        user, product, cnt = line.rstrip().split()
        if user not in d:
            d[user] = dict()
            d[user][product] = int(cnt)
        elif product not in d[user]:
            d[user][product] = int(cnt)
        else:
            d[user][product] += int(cnt)
for key in sorted(d.keys()):
    print(key + ':')
    for pr in sorted(d[key].keys()):
        print(pr, d[key][pr])
