# # Виртуальное окружение
# print("a")

# from colorama import Fore
# import sys
# from colorama import init, AnsiToWin32
# init(wrap=False)
# stream = AnsiToWin32(sys.stderr).stream

# def log_info(message):
#     print(f"{Fore.BLUE} [INFO] {Fore.RESET} {message}", file=stream)

# def log_warning(message):
#     print(f"{Fore.YELLOW} [WARNING] {Fore.RESET} {message}", file=stream)

# def log_error(message):
#     print(f"{Fore.RED} [ERROR] {Fore.RESET} {message}", file=stream)

import sys

def main():
    print(sys.argv)

if __name__ == "__main__":
    main()

folder_icon = '\U0001F4C1'
print(folder_icon)

