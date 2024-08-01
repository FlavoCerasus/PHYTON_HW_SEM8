# HOMEWORK - SEM 8 - Danil Eliseev

from csv import DictWriter, DictReader
from os.path import exists

class NameError(Exception):
    def __init__(self, txt):
        self.txt = txt

def get_data():     # Функция для ввода данных
    flag = False
    while not flag:
        try:
            first_name = input("Введите имя: ")
            if len(first_name) < 2:
                raise NameError("Слишком короткое имя!")
            last_name = input("Введите фамилию: ")
            if len(last_name) < 2:
                raise NameError("Слишком короткая фамилия!")
            phone = input("Введите номер телефона: ")
            if len(phone) < 11 or len(first_name) > 11:
                raise NameError("Номер телефона должен содержать 11 цифр!")
        except NameError as err:
            print(err)
        else:
            flag = True
    return [first_name, last_name, phone]


def create_file(file_name): # Функция по созданию файла
    with open(file_name, 'w', encoding='utf-8') as data:
        f_write = DictWriter(data, fieldnames=['ИМЯ', 'ФАМИЛИЯ', 'ТЕЛЕФОН'])
        f_write.writeheader()


def read_file(file_name): # Функция по выводу записи на экран
    with open(file_name, 'r', encoding='utf-8') as data:
        f_read = DictReader(data)
        return list(f_read)


def write_file(file_name, lst): # Функция по добавлению новых данных в файл
    res = read_file(file_name)
    obj = {'ИМЯ': lst[0], 'ФАМИЛИЯ': lst[1], 'ТЕЛЕФОН': lst[2]}
    res.append(obj)
    standart_write(file_name, res)

def row_search(file_name): # Функция позволяющая осуществлять поиск по фамилии
    last_name = input("Введите фамилию: ")
    res = read_file(file_name)
    for row in res:
        if last_name == row['ФАМИЛИЯ']:
            return row
    return "Запись не найдена"


def delete_row(file_name): # Функция по удалению конкретной строки
    row_number = int(input("Введите номер строки: "))
    res = read_file(file_name)
    res.pop(row_number-1)
    standart_write(file_name, res)


def standart_write(file_name, res):
    with open(file_name, 'w', encoding='utf-8') as data:
        f_write = DictWriter(data, fieldnames=['ИМЯ', 'ФАМИЛИЯ', 'ТЕЛЕФОН'])
        f_write.writeheader()
        f_write.writerows(res)


def change_row(file_name): # Функция по изменению строки
    row_number = int(input("Введите номер строки: "))
    res = read_file(file_name)
    data = get_data()
    res[row_number-1]['ИМЯ'] = data[0]
    res[row_number-1]['ФАМИЛИЯ'] = data[1]
    res[row_number-1]['ТЕЛЕФОН'] = data[2]
    standart_write(file_name, res)


def copy_to_another_file(file_name): # Функция по копированию строки в другой файл
    row_number = int(input("Введите номер строки, которую хотите скопировать: "))
    res = read_file(file_name)
    new_file_name = input("Назовите файл, в который произойдет копирование: ")
    create_file(new_file_name)
    res_new = read_file(new_file_name)
    res_new.append(res[row_number-1])
    standart_write(new_file_name, res_new)


file_name = 'phone.csv'

def main():
    while True:
        command = input("Введите команду: ")
        if command == "q":
            break
        elif command == "write":
            if not exists(file_name):
                create_file(file_name)
            write_file(file_name, get_data())
        elif command == "read":
            if not exists(file_name):
                print("Файл не существует. Создайте его.")
                continue
            print(read_file(file_name))
        elif command == "search":
            if not exists(file_name):
                print("Файл не существует. Создайте его.")
                continue
            print(row_search(file_name))
        elif command == "delete":
            if not exists(file_name):
                print("Файл не существует. Создайте его.")
                continue
            delete_row(file_name)
        elif command == "change":
            if not exists(file_name):
                print("Файл не существует. Создайте его.")
                continue
            change_row(file_name)
        elif command == "copy":
            if not exists(file_name):
                print("Файл не существует. Создайте его.")
                continue
            copy_to_another_file(file_name)
main()