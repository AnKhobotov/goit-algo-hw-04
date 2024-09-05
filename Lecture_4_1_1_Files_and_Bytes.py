# Работа с Файлами

# open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)

    # file - шлях до файлу у вигляді рядка. Це може бути повний шлях або шлях відносно поточного каталогу виконання.
    # mode (необов'язковий) - режим, в якому буде відкрито файл. Ось основні режими які ми будемо використовувати:
    # 'r' - читання (за замовчуванням). Файл має існувати.
    # 'w' - запис. Створює новий файл або перезаписує, що вже існує.
    # 'a' - додавання. Дописує в кінець файлу, не перезаписуючи його.
    # 'b' - бінарний режим (може бути використаний разом з іншими, наприклад 'rb' або 'wb').
    # '+' - оновлення (читання та запис).
    # buffering (необов'язковий) - визначає буферизацію: 0 для вимкненої, 1 для включеної буферизації рядків, більше 1 для вказання розміру буфера у байтах.
    # encoding (необов'язковий) - ім'я кодування, яке буде використовуватися для кодування або декодування файлу.
    # errors (необов'язковий) - вказує, як обробляти помилки кодування.
    # newline (необов'язковий) - контролює, як обробляються нові рядки.
    # closefd (необов'язковий) - має бути True (за замовчуванням); якщо вказано False, файловий дескриптор не буде закритий.
    # opener (необов'язковий) - визначає спеціальну функцію для відкриття файлу.


fh = open('test.txt', 'w')
symbols_written = fh.write('hello!')
print(symbols_written) # 6
fh.close()


fh = open('test.txt', 'w+')
fh.write('hello!')
fh.seek(0) # Возвращает указатель в начало файла

first_two_symbols = fh.read(2)
print(first_two_symbols)  # 'he'

fh.close()

fh = open('test.txt', 'w')
fh.write('hello!')
fh.close()

# Вывод по символьно
fh = open('test.txt', 'r')
while True:
    symbol = fh.read(1)
    if len(symbol) == 0:
        break
    print(symbol)

fh.close()

# Перезаписали в файл и прочиталь по-строчно

fh = open('test.txt', 'w')
fh.write('first line\nsecond line\nthird line')
fh.close()

fh = open('test.txt', 'r')
while True:
    line = fh.readline()
    if not line:
        break
    print(line)

fh.close()

# Вывод по-строчно + удаление знака переноса строки

fh = open("test.txt", "w")
fh.write("first line\nsecond line\nthird line")
fh.close()

fh = open("test.txt", "r")
lines = [el.strip() for el in fh.readlines()]
print(lines)

fh.close()

#   Метод Seek / Tell

fh = open("test.txt", "w+")
fh.write("hello!")

position = fh.tell()
print(position)  # 6

fh.seek(1)
position = fh.tell()
print(position)  # 1

fh.read(2)
position = fh.tell()
print(position)  # 3

fh.close()

# Try ... Except

fh = open('text.txt', 'w')
try:
    # Виконання операцій з файлом
    fh.write('Some data')
finally:
    # Закриття файлу в блоку finally гарантує, що файл закриється навіть у разі помилки
    fh.close()

# Менджер контексту With
    
with open('text.txt', 'w') as fh:
    # Виконання операцій з файлом
    fh.write('Some data')
# Файл автоматично закриється після виходу з блоку with


with open("test.txt", "w") as fh:
    fh.write("first line\nsecond line\nthird line")

with open("test.txt", "r") as fh:
    lines = [el.strip() for el in fh.readlines()]

print(lines)

# Работа с бинарными файлами

with open('raw_data.bin', 'wb') as fh:
    fh.write(b'Hello world!')

    # bytes - незмінний тип, що використовують для представлення байтів.
    # bytearray - змінний тип, що дозволяє модифікувати байти після їх створення.

s = b'Hello!'
print(s[1])  # Виведе: 101 (це ASCII-код символу 'e')

byte_string = b'Hello world!'
byte_str = 'some text'.encode()
print(byte_str)

# Перевод чисел в байт-строку

# Перетворення списку чисел у байт-рядок

numbers = [0, 128, 255]
byte_numbers = bytes(numbers)
print(byte_numbers)  # Виведе байтове представлення чисел

for num in [127, 255, 156]:
  print(hex(num))

# Кодирование символов

print(ord('a'))  # 97
print(chr(100))  # 'd'

s = "Привіт!"

utf8 = s.encode()
print(f"UTF-8: {utf8}")

utf16 = s.encode("utf-16")
print(f"UTF-16: {utf16}", type(utf16))

cp1251 = s.encode("cp1251")
print(f"CP-1251: {cp1251}")

s_from_utf16 = utf16.decode("utf-16")
print(s_from_utf16 == s)


# Відкриття текстового файлу з явним вказівкам UTF-8 кодування
# with open('example.txt', 'r', encoding='utf-8') as file:
#     content = file.read()
#     print(content)

# Массив байтов

byte_array = bytearray(b'Kill Bill')
byte_array[0] = ord('B')
byte_array[5] = ord('K')
print(byte_array)


byte_array = bytearray(b"Hello")
byte_array.append(ord("!"))  
print(byte_array)

byte_array = bytearray(b"Hello World")
string = byte_array.decode("utf-8")
print(string)  # Виведе: 'Hello World'


# Сравнение строк

string1 = "Hello World"
string2 = "hello world"
if string1.lower() == string2.lower():
    print("Рядки однакові")
else:
    print("Рядки різні")


text = "Python Programming"
print(text.casefold())

german_word = 'straße'  # В нижньому регістрі
search_word = 'STRASSE'  # В верхньому регістрі

# Порівняння за допомогою lower()
lower_comparison = german_word.lower() == search_word.lower()

# Порівняння за допомогою casefold()
casefold_comparison = german_word.casefold() == search_word.casefold()

print(f"Порівняння з lower(): {lower_comparison}")
print(f"Порівняння з casefold(): {casefold_comparison}")




















