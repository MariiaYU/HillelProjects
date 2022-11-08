# Запросить у пользователя 5 чисел и записать их в список

user_num = input("Enter 5 numbers: ").split()
num_list = [int(num.replace(",", "")) for num in user_num]

print(num_list)

# Дан список A = [1, 2, 3, 4, 5]. Удалить последнее число из списка
#
A = [1, 2, 3, 4, 5]
A.pop()
print(A)

# Запросить у пользователя 10 чисел и записать их в список A. Запросить у пользователя число N.
# Вывести пользователю сколько в списке A повторяется число N

user_num = input("Enter 10 numbers: ").split()
num_list = [int(num.replace(",", "")) for num in user_num]

n_num = input("Write down the number you want to check: ")

num_count = num_list.count(int(n_num))
print(f"Your number appears {num_count} times in the list")

# Запросить у пользователя число N. Запросить у пользователя N чисел и записать их в список A
# Вывести список в обратной последовательности

n = input("How much numbers do you want to write down?: ")
user_num = input(f"Enter {n} numbers: ").split()

num_list = [int(num.replace(",", "")) for num in user_num]

print(f"Your actual list: {num_list}.")
num_list.reverse()
print(f"Your reversed list: {num_list}")

# Запросить у пользователя 5 чисел и записать их в список A.
# Записать все числа из списка A которые больше 5 в список C

user_num = input(f"Enter 5 numbers: ").split()
num_list = [int(num.replace(",", "")) for num in user_num]

new_list = [num for num in num_list if num > 5]

print(f"Your new list: {new_list}")

# Запросить у пользователя число N. Запросить у пользователя N целых чисел и записать их в список A
# Найти в нем минимальное и максимальное число с помощью цикла (запрещено использовать функцию min, max, sorted, sort).
# Вывести эти числа.

n = input("How much numbers do you want to write down?: ")
user_num = input(f"Enter {n} numbers: ").split()
num_list = [int(num.replace(",", "")) for num in user_num]

max_num = 0
for num in num_list:
    if num > max_num:
        max_num = num

min_num = num_list[0]
for num in num_list:
    if num < min_num:
        min_num = num

print(f"Max num in your list is: {max_num}, min num is: {min_num}")

# Пользователь вводит текст нужно вывести количество чисел в этом тексте
# Пример: 'Lorem 222 ipsum, 123 dolor 1 sit amet. Количество чисел: 3

user_text = input("Enter your text: ").split()

num_list = []
for word in user_text:
    if word.isdigit():
        num_list.append(word)

print(f"Your text has {len(num_list)} numbers.")