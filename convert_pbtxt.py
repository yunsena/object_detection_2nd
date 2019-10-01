import os
import csv

# with open("label_map.pbtxt", 'r',encoding='UTF8') as f:
#     val = f.readlines()
#     print(val)

label = open("label_map.pbtxt", 'r',encoding='UTF8')
label = label.readlines()
# data = []
# for string in label:
#     data.append(string)
#     if "김밥" in string:
#         data.remove(string)
#
#         string = string.replace('"김밥"', '"gimbab"')
#         print(string)
#         data.append(string)
# print(label)

f = open('category.csv', 'r', encoding='utf-8')
rdr = csv.reader(f)
data = []
csv_data = {}
for line in rdr:
    # csv_data.append(line[0])
    # csv_data.append(line[1])
    csv_data[line[1]] = line[0]


for string in label:
    data.append(string)
    # print(string)
    if string.__contains__("name"):

        string_split = string.split('"')
        # print(string)
        # continue
        for line in csv_data.items():
            # print(string_split, line)
            if string_split[1] in line:
                print(string)
                data.remove(string)
                print(line)
                string1 = string.replace(line[0], line[1])
                print(string1)
                data.append(string1)
                print("------")
label = open("korean.pbtxt", 'w',encoding='UTF8')
for strings in data:
    label.writelines(strings)

# label = label.readlines()
# f.close()