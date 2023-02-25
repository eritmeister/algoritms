lst = list(map(int, input().split()))
all_neg = True
pos1, pos2, pos3, neg1, neg2 = 0, 0, 0, 0, 0
if len(lst) > 3:
    for i in lst:
        if i > 0:
            all_neg = False
        if i > pos1:
            pos3 = pos2
            pos2 = pos1
            pos1 = i
        elif i > pos2:
            pos3 = pos2
            pos2 = i
        elif i > pos3:
            pos3 = i
        elif i < neg1:
            neg2 = neg1
            neg1 = i
        elif i < neg2:
            neg2 = i
    if not all_neg:
        if neg1 * neg2 * pos1 >= pos1 * pos2 * pos3:
            print(neg1, neg2, pos1)
        else:
            print(pos1, pos2, pos3)
    else:
        neg1 = max(lst)
        lst.remove(neg1)
        neg2 = max(lst)
        lst.remove(neg2)
        neg3 = max(lst)
        print(neg1, neg2, neg3)
else:
    print(*lst)
