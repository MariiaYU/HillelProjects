# Дан файл с произвольным текстом, необходимо найти все числа в файле и записать в список numbers

with open("ex1.txt", "r") as file:
    file_data = file.read()

words = file_data.split()
numbers = [int(word) for word in words if word.isdigit()]
print(numbers)

# Запросить у пользователя текст и записать его в файл data.txt

user_text = input("Write down your text: ")

with open("ex2.txt", "w") as new_file:
    new_file.write(user_text)

# Запросить у пользователя число N и запросить N чисел у пользователя,
# потом записать их в файл numbers.txt через пробел
#
n = input("How much numbers do you want to write down?: ")
user_num = input(f"Enter {n} numbers: ").split()
num_list = [num.replace(",", "") for num in user_num]

with open("ex3.txt", "w") as num_file:
    for num in num_list:
        num_file.write(f"{num} ")

# Сгенерировать 100 рандомных чисел и записать их в файл random_numbers.txt, где одна строка = одно число

import random

with open("ex4.txt", "w") as random_file:
    for num in range(100):
        rand_num = random.randint(1, 10)
        random_file.write(f"{rand_num}\n")

# Дан файл с произвольным текстом, нужно найти количество слов в файле и вывести пользователю

with open("ex1.txt", "r") as words_file:
    words = words_file.read().split()

print(f"{len(words)} words in the file.")

# Дан файл в котором записаны числа через пробел, необходимо вывести пользователю сумму этих чисел

with open("ex3.txt", "r") as file:
    numbers_in_file = file.read().split()
    numbers = [int(num) for num in numbers_in_file]

print(sum(numbers))

# Дан файл в котором записан текст, необходимо вывести топ 5 строк которые чаще всего повторяются

from collections import Counter

with open("ex1.txt", "r") as file:
    words_in_file = file.read().split()

count = Counter(words_in_file)
list_most_common = count.most_common(5)
print(list_most_common)
