import csv

file = open("dataidi.csv" , "r" )
data = csv.reader(file)

data = list(data)
print(type(data))


headers = data[0]

data.pop(0)

print(data)

district = {}

#
#district= {hyd:["chaitu"]}
#temp = [chaitu]
#temp.append(pr32)
#temp = [chaut,pr32]
#{hyd:[chati,pr32]}
#
#district = {}
#temp = [chaitu]
#district[hyd] = [chatiu]
#district = {hyd:[chaitu]}

for i in data:
    if(i[2] in district):
        temp = district[i[2]]
        temp.append(i[0])
        district[i[2]] = temp
    else:
        temp = [i[0]]
        district[i[2]] = temp


print(district)