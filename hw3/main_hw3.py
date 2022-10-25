
# 1. Пользователь вводит с клавиатуры три числа в переменные a, b, c.
# Если все числа больше 10 и первые два числа делятся на 3, то вывести yes, иначе no

a = int(input("Enter number A: "))
b = int(input("Enter number B: "))
c = int(input("Enter number C: "))

if a > 10 and b > 10 and c > 10 and a % 3 == 0 and b % 3 == 0:
    print("yes")
else:
    print("no")

# 2. Пользователь вводит с клавиатуры три числа в переменные a, b, c.
# Найдите наибольшее число из них и запишите в переменную max.

a = int(input("Enter number A: "))
b = int(input("Enter number B: "))
c = int(input("Enter number C: "))

if a >= b and a >= c:
    max_num = a
elif b >= a and b >= c:
    max_num = b
elif c >= a and c >= b:
    max_num = c

print(f"The max number is: {max_num}")

# 3. Пользователь вводит два числа A и B, нужно вывести сумму всех четных чисел в диапазоне от A до B.

a = int(input("Enter number A: "))
b = int(input("Enter number B: "))

sum = 0
for each_num in range(a, b+1):
    sum += each_num

print(f"The sum of all numbers between {a} and {b} is: {sum}")







