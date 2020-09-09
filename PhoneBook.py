import csv
import re
from reformating_contact_list import contact_list

unique_contacts = {}
for contact in contact_list:
    id = contact[0]
    if id not in unique_contacts:
        unique_contacts[id] = contact
    else:
        for e in contact:
            if e not in unique_contacts[id]:
                unique_contacts[id].append(e)


def get_telephone_number():
    pattern_phone = r"[+]?\d{1}[ -]?[(]?(\d{3})[)]?[ -]?(\d{3})[ -]?(\d{2})[ -]?(\d{2})([ ]?[(]?((доб\.)[ ]?(\d+)\)))?"
    regex_phone = re.compile(pattern_phone)
    for list_ in unique_contacts.values():
        result = regex_phone.sub(r"+7-\1(\2)-\3-\4 \7\8", list_[5])
        list_[5] = result
    return unique_contacts.values()


cs = get_telephone_number()


def get_lastname():
    pattern_lastname = r"^([А-Я][а-я]*)(\,)?"
    regex_lastname = re.compile(pattern_lastname)
    for list_ in cs:
        result = regex_lastname.sub(r"\1, ", list_[0])
        list_[0] = result
    return cs


cs2 = get_lastname()


def get_name():
    pattern_name = r"([АВОИ][^Интеренет]\w+)(\ )"
    regex_name = re.compile(pattern_name)
    for list_ in cs2:
        result = regex_name.sub(r"\1, ", list_[1])
        list_[1] = result
    return cs2


cs3 = get_name()


def get_surname():
    pattern_surname = r"(\w*[в][и|н][ч|а])(\,+)"
    regex_surname = re.compile(pattern_surname)
    for list_ in cs3:
        result = regex_surname.sub(r"\1, ", list_[1])
        list_[1] = result
    return cs3


def write_accepted_phone_book():
    accepted_phone_book = cs3
    file = open("accepted_phone_book.csv", "w", encoding="utf-8")
    with file:
        writer = csv.writer(file)
        writer.writerows(accepted_phone_book)


print("Writing complete")

write_accepted_phone_book()
