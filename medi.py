import csv

file = open("medi.csv", "r")

file_contents = csv.reader(file)

file_contents = list(file_contents)


header = file_contents[0]

file_contents.pop(0)


surgury = {}


for i in file_contents:
    if (i[2] in surgury):
        temp = surgury[i[2]]
        temp.append(i[0])
        surgury [i[2]] = temp

    else:
        temp = [i[0]]
        surgury[i[2]] = temp


 # print (surgury)



location = {}


for i in file_contents:
    if (i[3] in location):
        temp = location[i[3]]
        temp.append(i[0])
        temp.append(i[2])
        location[i[3]] = temp

    else:

        temp = [i[0]]
        temp.append(i[2])
        location[i[3]] = temp



 print (location)



# zip_code = {}
#
#
# for i in file_contents:
#     if (i[6] in zip_code):
#         temp = zip_code[i[6]]
#         temp.append(i[0])
#         temp.append(i[1])
#         temp.append(i[2])
#         temp.append(i[3])
#         temp.append(i[4])
#         temp.append(i[5])
#         zip_code[i[6]] = temp
#
#     else:
#         temp = [i[0]]
#         temp.append(i[1])
#         temp.append(i[2])
#         temp.append(i[3])
#         temp.append(i[4])
#         temp.append(i[5])
#         zip_code[i[6]] = temp
#


# print(zip_code)



