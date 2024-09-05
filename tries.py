from pathlib import Path, PurePath
import colorama
import sys

# with open("test1.txt", "w") as fh:
#     fh.write("Korp,3000\nBorisenko,2000\nRaju,1000\nKo,3500\nKMo,31000.67\n")

# rel_path = Path("./test1.txt")
# abs_path = rel_path.absolute()
# print(abs_path)
# # rel_path.unlink(missing_ok=True)
# with open("test1.txt", "r") as fh:
#     lines = [el.strip() for el in fh.readlines()]
#     lines = dict([el.split(",") for el in lines])
#     print(lines)
#     c = lines.values()
#     a = []
#     total = 0
#     for i in c:
#         i = float(i)
#         a.append(i)
#         total += i 
#     # a= tuple(total)
#     average = total/len(c)
#     print(c,total, a,len(c))
    
# with open("text.txt", "w") as fh:
#     fh.write("60b90c1c13067a15887e1ae1,Tayson,3\n60b90c2413067a15887e1ae2,Vika,1\n60b90c2e13067a15887e1ae3,Barsik,2\n60b90c3b13067a15887e1ae4,Simon,12\n60b90c4613067a15887e1ae5,Tessi,5\n")        
    
def get_cats_info(path):

    try:
        path = Path(path)
        b=[]
        with open(path, "r", encoding="utf-8", errors="string") as fh:
            lines = [el.strip() for el in fh.readlines()]
            lines = [el.split(",") for el in lines]
            for el in lines:
                a= dict()
                a['id']=el[0]
                a['name'] = el[1]
                a['age'] = el[2]
                b.append(a)
                # print(b)
    except Exception as e:
        print(e)
    # finally:
    #     print(b)
    # print(b)
        
cats_info = get_cats_info("./text.txt")
print(cats_info)


# get_cats_info(Path)
# import sys

# def main():
#     print(sys.argv)

# if __name__ == "__main__":
#     main()
                
    # def func(Path):
    #     rel_path = Path("./New")
    #     abs_path = rel_path.absolute()
    #     print(abs_path)

# def obhod(path):
#     path = Path
#     path = sys.argv()

#     print(sys.argv)
#         # if path.exists():
#         #     print(f"{path} існує")
#         # with open(path, "r"):
#         #     for i in path:
#     if path.is_dir:
#         path.walkdir()
#     print(dir)

    # obhod(Path)




# ___________________Colorama_____________
import math
from colorama import Fore
# from Video_module_4 import log_info, log_warning, log_error
import sys
from colorama import init, AnsiToWin32
init(wrap=False)
stream = AnsiToWin32(sys.stderr).stream
print(Fore.BLUE + 'blue text on stderr',Fore.RESET, file=stream)
# print(Style.RESET_ALL, file=stream)


# def calculate_square_root(numbers: list) -> None:
#     for number in numbers:
#         try:
#             if number < 0:
#                 # Логування попередження для від'ємних чисел
#                 log_warning(f"Знайдено від'ємне число: {number}. Пропускаємо.")
#                 continue

#             root = math.sqrt(number)
#             log_info(f"Квадратний корінь з {number} - {root:.2f}")

#         except Exception as e:
#             # Логування помилки у випадку інших винятків
#             log_error(f"Помилка при обчисленні кореня для {number}: {e}")

# if __name__ == "__main__":
#     # Припустимо, у нас є список чисел
#     numbers = [16, -4, 9, 25, 0, 4,"16"]
#     calculate_square_root(numbers)

# import sys
# from colorama import init, AnsiToWin32
# init(wrap=False)
# stream = AnsiToWin32(sys.stderr).stream
# print(Fore.BLUE + 'blue text on stderr', file=stream)

# from colorama import Fore, Back, Style

# print(f"{Fore.RED} + 'Це червоний текст'", file=stream)
# print(Back.GREEN + 'Це текст на зеленому фоні', file=stream)
# print(Style.RESET_ALL, file=stream)
# print('Це звичайний текст після скидання стилю')

# folder_icon = bytes(226148163)
# print(folder_icon.decode())


