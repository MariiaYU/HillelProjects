# Запросить у пользователя число N - ширина треугольника.
# Вывести треугольник с шириной N с помощью цикла.

triangle_width = int(input("Enter triangle width: "))

print("1)")
for each_line in range(triangle_width, 0, -1):
    print("*" * each_line)

print("2)")
for each_line in range(1, triangle_width+1):
    print("*" * each_line)

print("3)")
for each_line in range(triangle_width, 0, -1):
    print((" " * (triangle_width-each_line)) + ("*" * each_line))

print("4)")
for each_line in range(1, triangle_width+1):
    print((" " * (triangle_width-each_line)) + ("*" * each_line))




