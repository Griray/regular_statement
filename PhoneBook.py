# from pprint import pprint
import re
import csv

with open("phonebook_raw.csv", encoding='utf-8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)


def get_lastname():
    lastname = []
    pattern_lastname = r"^([А-Я][а-я]*)"
    regex_lastname = re.compile(pattern_lastname)
    for elements in contacts_list[1:]:
        inform = re.findall(regex_lastname, elements[0])
        lastname.append(inform)
    return lastname


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


def get_telephone_number():
    phone = []
    pattern_phone = r"((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?([\d\- ]\d+)"
    regex_phone = re.compile(pattern_phone)
    for elements in contacts_list[1:]:
        inform = re.findall(regex_phone, str(elements))
        result =pattern_phone.sub()
    return phone

print(get_telephone_number())
