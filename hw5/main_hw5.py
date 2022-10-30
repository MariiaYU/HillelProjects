# 1. Пользователь вводит слово, если это слово является полиндромом, то вывести '+', иначе '-'

user_word = input("Write your word: ").lower()

if user_word == user_word[::-1]:
    print("+")
else:
    print("-")

# 2. Пользователь вводит текст и слово которое нужно найти, если это слово есть в тексте, вывести 'YES', иначе 'NO'

text = input("Enter your text: ")
word = input("What word are you looking for in the text?: ")
if text.find(word) != -1:
    print("Yes")
if text.find(word) == -1:
    print("No")

# 3. Пользователь вводит строку. Если она начинается на 'abc', то заменить их на 'www', иначе добавить в конец строки 'zzz'.

user_text = input("Yor message: ").lower()

if user_text.startswith("abc"):
    new_text = user_text.replace(user_text[0:2], "www")
    print(f"Your new message: {new_text}")
else:
    print(f"Your new message: {user_text}" + "zzz")

# 4. Пользователь вводит текст, удалить в тексте все цифры и вывести строку пользователю.
#
user_text = input("Enter your text: ")
new_text = ""

for each_character in user_text:
    if not each_character.isdigit():
        new_text += each_character

print(f"Your text without digits is: {new_text}")

# 5. Написать валидатор для почты. Пользователь вводит почту, а программа должна проверить,
#    что в почте есть символ '@' и '.', и если это так, то вывести "YES", иначе "NO"

user_email = input("Enter your email: ")

if user_email.find("@") != -1 and user_email.rfind(".", user_email.find("@"), -1) != -1 and user_email.find("@") > 0:
    print("Your email is correct.")
else:
    print("Your email is incorrect.")







