st1 = set(map(int, input().split()))
st2 = set(map(int, input().split()))
print(*sorted(st1 & st2))
