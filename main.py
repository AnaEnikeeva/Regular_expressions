import csv
import re
from pprint import pprint


path = r'C:\Users\Анастасия\OneDrive\Рабочий стол\regular_expressions\phonebook_raw.csv'
with open(path, encoding="utf-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)


correct_number = r'(\+7|8)*[\s\(]*(\d{3})[\)\s-]*(\d{3})[-]*(\d{2})[-]*(\d{2})[\s\(]*(доб\.)*[\s]*(\d+)*[\)]*'
phone = r'+7(\2)-\3-\4-\5 \6\7'


newlist = []
for name in contacts_list:
    new = []
    del_empty = []
    list = (" ".join(name[:3])).strip().split(" ")
    for m in list:
        if len(m) >= 1:
            del_empty.append(m)
   
    if len(del_empty) == 3:
        new.append(list)
        for line in new:
            collect = [del_empty[0], del_empty[1], del_empty[2], name[3], name[4],
                  re.sub(correct_number, phone , name[5]),
                  name[6]]
        newlist.append(collect)
        # print(newlist)




dict = {}
for names in newlist:
    key = f'{names[0]} {names[1]}'
    if key not in dict:
        dict[key] = names
    else:
        for i in range(len(names)):
            if dict[key][i] == "":
                dict[key][i] = names[i]
new_phonebook = [value for value in dict.values()]
# print(dict)





path = r'C:\Users\Анастасия\OneDrive\Рабочий стол\regular_expressions\phonebook.csv'
with open(path, "w", encoding="utf-8") as f:
  datawriter = csv.writer(f, delimiter=',')
  # Вместо contacts_list подставьте свой список
  datawriter.writerows(new_phonebook)
