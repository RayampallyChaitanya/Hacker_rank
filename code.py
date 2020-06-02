file = open('98-0.txt', 'r', encoding='utf-8')
stop_words_file = open('stopwords','r',encoding='utf-8')

dict = {}

file_content = file.read().lower().split()

stop_words = stop_words_file.read().lower().split()

# print(stop_words)

# print(type(file_content))
# print(file_content)

# {received:3,for:5, and:8}




for i in file_content:
    i = i.replace(":","")
    if i == "," or i == "." or i == "?" or i == '"' or i==":":
        continue

    if i in stop_words:
        continue

    if i in dict:
        dict[i] = dict[i]+1
    else:
        dict[i] = 1

for i in dict:
    print(i+" : "+str(dict[i]))