import re
import csv

with open("phonebook_raw.csv", encoding='utf-8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)


merge_dict = {}
list_sur = []
list_inform = []
for elements in contacts_list:
    elements[0] = elements[0].split(" ")
    keys = elements[0][0]
    list_sur.append(keys)
    values = elements[0:]
    list_inform.append(values)


def get_telephone_number():
    pattern_phone = r"[+]?\d{1}[ -]?[(]?(\d{3})[)]?[ -]?(\d{3})[ -]?(\d{2})[ -]?(\d{2})([ ]?[(]?((доб\.)[ ]?(\d+)\)))?"
    regex_phone = re.compile(pattern_phone)
    for list_ in contacts_list:
        result = regex_phone.sub(r"+7-\1(\2)-\3-\4 \7\8", list_[5])
        list_[5] = result
    return contacts_list


contacts_list_1 = get_telephone_number()

def get_lastname():
    pattern_lastname = r"^([А-Я][а-я]*)(\,)?"
    regex_lastname = re.compile(pattern_lastname)
    for list_ in contacts_list_1:
        result = regex_lastname.sub(r"\1, ", list_[0])
        list_[0] = result
    return contacts_list_1

contacts_list_2 = get_lastname()


def get_name():
    pattern_name = r"([АВОИ][^Интеренет]\w+)(\ )"
    regex_name = re.compile(pattern_name)
    for list_ in contacts_list_2:
        print(list_[0])
        result = regex_name.sub(r"\1, ", list_[1])
        list_[1] = result
    return contacts_list_2

print(get_name())

def get_surname():
    pattern_surname = r"(\w*[в][и|н][ч|а])(\,+)"
    regex_surname = re.compile(pattern_surname)
    for list_ in contacts_list_2:
        result = regex_surname.sub(r"\1, ", list_[1])
        list_[1] = result
    return contacts_list_2


