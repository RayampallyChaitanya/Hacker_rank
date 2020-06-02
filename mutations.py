string = input()

lis = list(string)

n = input().split()

n[0] = int(n[0])
lis[n[0]] = n[1]

str1 = "".join(lis)

print(str1)