n = int(input())

my_list = input().split()

my_list = list(map(int,my_list))

my_list = sorted(my_list)
factor = []

for i in range(1,my_list[0]+1):
    if (my_list[0]%i == 0):
        factor.append(i)

l = len(factor)

for j in range(1,n):
    for k in range(l):
        if(my_list[j]%factor[k]!=0):
            factor.pop(k)
            l = l-1

    print(l)


print(factor)