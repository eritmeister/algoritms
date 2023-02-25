lst = list(map(int, input().split()))
pos1, pos2, neg1, neg2 = 0, 0, 0, 0
if len(lst) > 2:
    for i in lst:
        if i > pos1:
            pos2 = pos1
            pos1 = i
        elif i > pos2:
            pos2 = i
        if i < neg1:
            neg2 = neg1
            neg1 = i
        elif i < neg2:
            neg2 = i
    if neg1 * neg2 > pos1 * pos2:
        print(neg1, neg2)
    else:
        print(pos2, pos1)
else:
    if lst[0] < lst[1]:
        print(*lst)
    else:
        print(lst[1], lst[0])
