dct = dict()
with open('input.txt') as f:
    for line in f:
        for word in line.split():
            if len(word) > 0:
                if word not in dct:
                    dct[word] = 0
                else:
                    dct[word] += 1
most_common = word
maximum = 0
for word in dct.keys():
    if dct[word] > maximum:
        maximum = dct[word]
        most_common = word
    elif dct[word] == maximum and word < most_common:
        most_common = word
print(most_common)
