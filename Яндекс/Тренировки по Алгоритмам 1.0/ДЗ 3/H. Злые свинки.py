st = set()
n = int(input())
for _ in range(n):
    x, y = list(map(int, input().split()))
    st.add(x)
print(len(st))
