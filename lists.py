n = int(input())

list_final = []

for i in range(n):
    action, *line = input().split()
    numbers = list(map(int, line))

    if action == 'insert' :
        list_final.insert(numbers[0] , numbers[1])
    elif action == 'print' :
        print(list_final)

    elif action == 'remove':
        list_final.remove(numbers[0])

    elif action == 'append' :
        list_final.append(numbers[0])

    elif action == 'sort' :
        list_final.sort()

    elif action == 'pop' :
        list_final.pop()

    elif action == 'reverse' :
        list_final.reverse()
