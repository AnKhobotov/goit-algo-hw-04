# Работа с архивами
# Модуль shutil

# shutil.make_archive(base_name, format, root_dir=None, base_dir=None)

    # base_name - шлях до файлу, де потрібно зберегти архів, без розширення.
    # format - формат архіву, наприклад 'zip', 'tar', 'gztar', 'bztar' або 'xztar'.
    # root_dir - директорія, з якої буде створено архів. Якщо не вказано, використовується поточна директорія.
    # base_dir - директорія всередині архіву, з якої почнеться архівація.

import shutil

# Створення ZIP-архіву з вмістом директорії 'my_folder'
shutil.make_archive('example', 'zip', root_dir='my_folder')


# shutil.unpack_archive(filename, extract_dir=None, format=None)

    # filename - шлях до архівного файлу, який потрібно розпакувати.
    # extract_dir - директорія, куди буде розпаковано вміст архіву. Якщо не вказано, використовується поточна директорія.
    # format - формат архіву наприклад, zip, tar, gztar, bztar, або xztar. Якщо параметр не вказано, Python намагається визначити формат автоматично.

import shutil

# Розпакування ZIP-архіву в певну директорію
# shutil.unpack_archive('example.zip', 'destination_folder')

        # shutil.copy(src, dst) копіює файл з src в dst. Якщо dst є директорією, файл буде скопійований зі своїм поточним іменем у цю директорію.
        # shutil.copytree(src, dst) рекурсивно копіює всю директорію src в директорію dst.
        # shutil.move(src, dst) переміщує файл або директорію src в dst.
        # shutil.rmtree(path) рекурсивно видаляє директорію path.
        # shutil.disk_usage(path) повертає статистику використання диска, що містить загальний об'єм, використаний об'єм і вільний об'єм для даного шляху.



# Модуль Pathlib

from pathlib import PurePath

p = PurePath("/usr/bin/simple.jpg")
print("Name:", p.name)  
print("Suffix:", p.suffix) 
print("Parent:", p.parent)

    # p.parent вказує на батьківську директорію;
    # p.name повертає лише рядок з ім'ям директорі або файлу, на який вказує p;
    # p.suffix повертає рядком розширення файлу, на який вказує p, починаючи з крапки;

from pathlib import Path

p = Path("example.txt")
p.write_text("Hello, world!")
print(p.read_text()) 
print("Exists:", p.exists()) 

# Для Windows
path_windows = Path("C:/Users/Username/Documents/file.txt")


# Початковий шлях
base_path = Path("/usr/bin")

# Додавання додаткових частин до шляху
full_path = base_path / "subdir" / "script.py"

print(full_path)  # Виведе: /usr/bin/subdir/script.py


# Перетворення відносного шляху в абсолютний
relative_path = Path("documents/example.txt")
absolute_path = relative_path.absolute()
print(absolute_path)



# Початковий шлях до файлу
original_path = Path("documents/example.txt")

# Зміна імені файлу
new_path = original_path.with_name("report.txt")
print(new_path)



original_path = Path("documents/example.txt")

# Створює новий об'єкт Path з іншим ім'ям файлу
# new_path = original_path.with_name("report.txt")
# original_path.rename(new_path)

# Path.read_text(encoding=None, errors=None)

    # encoding - необов'язковий, ім'я кодування, яке використовується для декодування файлу. Якщо не вказано, використовується кодування за замовчуванням.
    # errors - необов'язково, інструкція, як обробляти помилки декодування.

# Path.write_text(data, encoding=None, errors=None)

    # data - рядок, який необхідно записати в файл.
    # encoding - необов'язковий, ім'я кодування, яке використовується для декодування файлу. Якщо не вказано, використовується кодування за замовчуванням.
    # errors - необов'язково, інструкція, як обробляти помилки декодування.

    # errors='strict'. Це значення за замовчуванням. Якщо виникає помилка декодування, буде викинуто виключення UnicodeDecodeError.
    # errors='ignore'. Якщо ми хочемо ігнорувати помилки декодування. Частини тексту, що не можуть бути декодовані, будуть просто пропущені.
    # errors='replace'. Якщо пропускати ми не хочемо, то замінимо неможливі для декодування символи на спеціальний символ заміни, згідно документації символ '?'.


# Створення об'єкту Path для файлу
file_path = Path("example.txt")

# Запис тексту у файл
file_path.write_text("Привіт світ!", encoding="utf-8")


# Створення об'єкту Path для файлу
file_path = Path("example.txt")

# Читання тексту з файлу
text = file_path.read_text(encoding="utf-8")
print(text)


# Створення об'єкту Path для бінарного файлу
file_path = Path("example.bin")

# Бінарні дані для запису
data = b"Python is great!"

# Запис байтів у файл
file_path.write_bytes(data)


# Створення об'єкту Path для бінарного файлу
file_path = Path("example.bin")

# Читання байтів з файлу
binary_data = file_path.read_bytes()
print(binary_data)


# Створення об'єкту Path для директорії
directory = Path("./New")

# Виведення переліку всіх файлів та піддиректорій
for path in directory.iterdir():
    print(path)

# Создание новой директории
    # Path.mkdir(mode=0o777, parents=False, exist_ok=False)
    #     mode - права доступу до директорії, використовуються для Linux і не актуальні для Windows.
    # parents - якщо має значення True, створить всі батьківські директорії, які відсутні.
    # exist_ok - якщо має значення True, помилка не буде викинута, якщо директорія вже існує.


directory = Path('/my_directory/new_folder')
directory.mkdir(parents=True, exist_ok=True)

    # метод exists() перевіряє, чи існує файл або директорія.
    # метод is_dir() перевіряє, чи є об'єкт директорією.
    # метод is_file() перевіряє, чи є об'єкт файлом.


path = Path("./New")

# Перевірка існування
if path.exists():
    print(f"{path} існує")

# Перевірка, чи це директорія
if path.is_dir():
    print(f"{path} є директорією")

# Перевірка, чи це файл
if path.is_file():
    print(f"{path} є файлом")

import shutil


# Вихідний і цільовий файли
# source = Path('/path/to/source/file.txt')
# destination = Path('/path/to/destination/file.txt')

# Копіювання файла
# shutil.copy(source, destination)

# shutil.copy Копирует только содержимое файла и не копирует метаданные
# shutil.copy2 Копирует все с метаданными

# Метод shutil.move перемщает данные


    # # Вихідний і цільовий шляхи
    # source = Path('/path/to/source/file.txt')
    # destination = Path('/path/to/destination/file.txt')

    # # Переміщення файла
    # shutil.move(source, destination)

# Метод stat()

import time

file_path = Path("./New")

# Час створення та модифікації
creation_time = file_path.stat().st_ctime
modification_time = file_path.stat().st_mtime

print(f"Час створення: {time.ctime(creation_time)}")
print(f"Час модифікації: {time.ctime(modification_time)}")



# Створення об'єкту Path для файлу
file_path = Path('./raw_data.bin')

# Перевірка, чи файл існує, перш ніж видаляти
if file_path.exists():
    file_path.unlink()
    print(f'Файл {file_path} було видалено')
else:
    print(f'Файл {file_path} не існує')


file_path = Path('./path/to/file.txt')
file_path.unlink(missing_ok=True)


















