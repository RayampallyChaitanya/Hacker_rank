from itertools import combinations_with_replacement

In = input().split()

n = int(In[-1])

s = list(In[0])

temp = list(combinations_with_replacement(sorted(s),n))

temp.sort()
for elements in temp:
    print(*elements, sep='')