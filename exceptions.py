n = int(input())
l = []
for i in range(n):
    l.append(input().split())

for i in range(len(l)):
    a = l[i][0]
    b = l[i][1]
    try:
        print (int(a) // int(b))
    except ZeroDivisionError as e:
        print("Error Code:", e)
    except ValueError as e:
        print("Error Code:", e)