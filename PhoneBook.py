import re
import csv

with open("phonebook_raw.csv", encoding='utf-8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)


def get_telephone_number():
    counter = 1
    pattern_phone = r"[+]?\d{1}[ -]?[(]?(\d{3})[)]?[ -]?(\d{3})[ -]?(\d{2})[ -]?(\d{2})([ ]?[(]?((доб\.)[ ]?(\d+)\)))?"
    regex_phone = re.compile(pattern_phone)
    for list in contacts_list[1:]:
        result = regex_phone.sub(r"+7-\1(\2)-\3-\4 \7\8", str(list))
        contacts_list[counter] = result
        counter += 1
    return contacts_list


phone_list = get_telephone_number()


def get_lastname():
    counter = 0
    pattern_lastname = r"^([А-Я][а-я]*)(\,)?"
    regex_lastname = re.compile(pattern_lastname)
    for elements in phone_list:
        result = regex_lastname.sub(r"\1\, ", str(elements))
        phone_list[counter] = result
        counter += 1
    return phone_list



def get_surname():
    surname = []
    pattern_surname = r"\w*[в][и|н][ч|а]"
    regex_surname = re.compile(pattern_surname)
    for elements in contacts_list[1:]:
        inform = re.findall(regex_surname, str(elements))
        surname.append(inform)
    return surname


def get_name():
    name = []
    pattern_name = r"([АВОИ][^Интеренет]\w+\s)"
    regex_name = re.compile(pattern_name)
    for elements in contacts_list[1:]:
        inform = re.findall(regex_name, str(elements))
        name.append(inform)
    return name

