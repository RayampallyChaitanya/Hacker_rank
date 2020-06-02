from itertools import combinations

In = input().split()
s = In[0]
s = list(s)
n = In[-1]
n = int(n)
for i in range(n):
    temp = list(combinations(sorted(s),i+1))
    temp.sort()
    for elements in temp:
        print(*elements, sep='')

