lang_all = set()
lang_every = set()
is_empty = True
n = int(input())
for i in range(n):
    lang_stud = set()
    m = int(input())
    for j in range(m):
        lang = input()
        lang_stud.add(lang)
    lang_all = lang_all.union(lang_stud)
    if is_empty:
        is_empty = False
        lang_every = lang_stud
    else:
        lang_every = lang_every.intersection(lang_stud)
print(len(lang_every))
for lang in lang_every:
    print(lang)
print(len(lang_all))
for lang in lang_all:
    print(lang)
