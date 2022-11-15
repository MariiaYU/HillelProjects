# 1. Напишите функцию change(lst), которая принимает список и меняет местами его первый и последний элемент.
# В исходном списке минимум 2 элемента.

def change(list):
    list[0], list[-1] = list[-1], list[0]
    print(list)


num_list = [1, 2, 3, 4]

change(num_list)

# Напишите функцию to_dict(lst), которая принимает аргумент в виде списка и возвращает словарь,
# в котором каждый элемент списка является и ключом и значением.
# Предполагается, что элементы списка будут соответствовать правилам задания ключей в словарях.

def to_dic(list):
    dict = {key: key for key in list}
    print(dict)


num_list = [1, 2, 3, 4]
to_dic(num_list)

# Напишите функцию sum_range(start, end), которая суммирует все целые числа от значения «start» до величины «end» включительно.
# Если пользователь задаст первое число большее чем второе, просто поменяйте их местами.


def sum_range(start, end):
    sum = 0
    if start > end:
        start, end = end, start
    for num in range(int(start), int(end)+1):
        sum += num
    print(sum)


sum_range(0, 5)

# Напишите функцию read_last(lines, file), которая будет открывать определенный файл file
# и выводить на печать построчно последние строки в количестве lines
# (на всякий случай проверим, что задано положительное целое число).


def read_last(lines, file):
    if lines >= 0:
        with open(file, "r") as file_to_read:
            lines_to_read = file_to_read.readlines()
            needed_lines = lines_to_read[-int(lines):]
        if int(lines) <= len(lines_to_read):
            for num in range(int(lines)):
                print(needed_lines[num])
        else:
            print("'Lines' should be less than or equal to the number of all lines in the text file.")
    else:
        print("'Lines' should be a positive number.")


read_last(4, "text.txt")
