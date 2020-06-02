tools = input()

tools = list(tools)

n = int(input())

final = [tools[i * n:(i + 1) * n] for i in range((len(tools) + n - 1) // n )]

for i in range(len(final)):
    s =  ''.join(sorted(set(final[i]), key=final[i].index))
    print(s)