nAndm = input().split()
nAndm = list(map(int,nAndm))

n = nAndm[0]
m = nAndm[1]

arr = input().split()
arr = map(int,arr)

nlis = input().split()
mlis = input().split()

nlis = set(map(int,nlis))
mlis = set(map(int,mlis))

happiness = 0

for i in arr:
    if i in nlis:
        happiness = happiness + 1
    elif i in mlis:
        happiness = happiness - 1

print(happiness)