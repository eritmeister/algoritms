dct = dict()
n = int(input())
for _ in range(n):
    word1, word2 = input().split()
    dct[word1] = word2
    dct[word2] = word1
print(dct[input()])
