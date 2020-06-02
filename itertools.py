from itertools import product

A = input().split()
B = input().split()

A = list(map(int,A))
B = list(map(int,B))

prod = list(product(A,B))

print(*prod, sep=" ")



