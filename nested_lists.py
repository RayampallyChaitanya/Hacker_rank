n = int(input())
students = []
temp = []
for i in range(n):
    temp.append(input())
    temp.append(float(input()))

def chunks(l, n):
    return [l[i:i+n] for i in range(0, len(l), n)]
chunks(temp,2)

print(temp)
