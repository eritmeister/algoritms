A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())
if A <= D and B <= E or \
   B <= D and A <= E or \
   A <= D and C <= E or \
   C <= D and A <= E or \
   B <= D and C <= E or \
   C <= D and B <= E:
    print('YES')
else:
    print('NO')
