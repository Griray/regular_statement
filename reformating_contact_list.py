import csv

with open("phonebook_raw.csv", encoding='utf-8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)


def count_words(contact_list):
    count = 0
    flag = 0
    counter = 1
    for i in range(len(contacts_list)):
        if contact_list[i][0] != ' ' and flag == 0:
            count += 1
            flag = 1
            counter += 1
        else:
            if contact_list[i] == ' ':
                flag = 0
    return count


def do_normal_contact_list():
    for list_ in contacts_list[1:]:
        lenght = len(list_[0].split())
        lenght_second = len(list_[1].split())
        if lenght == 3:
            first_part = list_[0].split()
            del list_[0]
            list_.insert(0, first_part[0])
            list_.insert(1, first_part[1])
            list_.insert(2, first_part[2])
            del list_[3: 5]
        elif lenght == 2:
            second_part = list_[0].split()
            del list_[0]
            list_.insert(0, second_part[0])
            list_.insert(1, second_part[1])
            del list_[2]
        elif lenght_second == 2:
            third_part = list_[1].split()
            del list_[1]
            list_.insert(1, third_part[0])
            list_.insert(2, third_part[1])
            del list_[3]
        else:
            del list_[7]
    return contacts_list


contact_list = do_normal_contact_list()
