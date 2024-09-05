from pathlib import PurePath

from pathlib import Path

p = Path("example.txt")
p.write_text("Hello, world!")
print(p.read_text()) 
print("Exists:", p.exists()) 
import sys

def main():
    print(sys.argv)

if __name__ == "__main__":
    main()

original_path = Path("documents/example.txt")
print(original_path)
# a= (U+2523)

# def a(path = Path(input("DD  "))):
#     # path = input("DD  ")
#     return path
# folder = '\U0001F4C1'
# a = '\U000002EB'

# import sys

# def main():
#     path = sys.argv[1]
#     return path

# if __name__ == "__main__":
#     main()

from colorama import init, AnsiToWin32, Fore, Back, Style
init(wrap=True)
stream = AnsiToWin32(sys.stderr).stream

def rec(path, level = 0):
    # path = sys.argv[1]
    folder = '\U0001F4C1'
    a = '\U00002516'
    
    directory = Path(path)
    # print(directory)
    # level = 0

    # print(directory.name)
    for path in directory.iterdir():
        
        if path.is_dir():
            level += 1
            if level == 1:
                print( f"{Fore.MAGENTA}{a * level}{folder} Папка: {path.name},{Style.RESET_ALL} ур {level}",file=stream)
            if level > 1:
                print( f"{Fore.MAGENTA}{' ' * (level-1)*4}{a * (level-1)}{folder} Папка:{path.name}, ур {level}{Style.RESET_ALL}",file=stream)
            
            rec(path, level)     
            # print(f"| Папка:{path.name}, ур {level}")
            level -= 1 
        if path.is_file():
            level += 1
            # print(level)
            if level == 1:
                print( f"{'-' * level} файл:{path.name}, ур {level}")
            if level > 1:
                print( f"{' '*4*(level-1) + a} файл:{path.name}, ур {level}")
                # print(path)
    # print(path.name)    

rec(sys.argv[1])        

