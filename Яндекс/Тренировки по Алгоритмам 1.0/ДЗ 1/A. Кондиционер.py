t_room, t_cond = list(map(int, input().split()))
mode = input()
if mode == 'fan':
    print(t_room)
elif mode == 'auto':
    print(t_cond)
elif mode == 'heat':
    if t_cond > t_room:
        print(t_cond)
    else:
        print(t_room)
elif mode == 'freeze':
    if t_cond < t_room:
        print(t_cond)
    else:
        print(t_room)
