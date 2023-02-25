dct = dict()
res = list()
with open('input.txt') as f:
    for line in f:
        for word in line.split():
            if len(word) > 0:
                if word not in dct:
                    dct[word] = 0
                else:
                    dct[word] += 1
                res.append(str(dct[word]))
print(' '.join(res))
