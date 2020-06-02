file = open("dash.txt" , "r" , encoding= "utf-8")

file_contents = file.read().lower()

letter_dict = {}

for i in file_contents:

    if i in letter_dict:
        letter_dict[i] = letter_dict[i] + 1

    else:
        letter_dict[i] = 1



for i in letter_dict:
    print(i + " : " + str(letter_dict[i]))

