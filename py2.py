# import os

# def print_directory_tree(startpath, folder_icon='📁', file_icon='📄'):
#     for root, dirs, files in os.walk(startpath):
#         level = root.replace(startpath, '').count(os.sep)
#         indent = ' ' * 4 * level
#         print(f'{indent}{folder_icon} {os.path.basename(root)}')
#         sub_indent = ' ' * 4 * (level + 1)
#         for file in files:
#             print(f'{sub_indent}{file_icon} {file}')

# # Укажите путь к директории, структуру которой вы хотите отобразить
# startpath = './New'
# print_directory_tree(startpath)

from pathlib import Path

def rec(path):

    directory = Path(path).absolute()
    
    for path in directory.iterdir():
        
        level = 0
        if path.is_dir:
            level += 1
            # print(f"| Папка:{path.name}, ур {level}")
            rec(path)     
            # print(f"| Папка:{path.name}, ур {level}")
            level -= 1 
        if path.is_file():
            level += 1
            # print(level)
            print(f"     Файл: {path.name}, ур {level}")
                # print(path)
    print(path.name)    

rec ("./New")   
