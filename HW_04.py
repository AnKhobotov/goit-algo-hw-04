from pathlib import Path
import math

# Task 1

def total_salary(path):
    try:
        with open(path, "r", encoding='utf-8',errors="strict") as fh:
            lines = [el.strip() for el in fh.readlines()]
            lines = dict([el.split(",") for el in lines])
            lines = lines.values()
            total = 0
            for i in lines:
                i = float(i)
                total += i 
            average = total/len(lines)
        return total, average  
    except Exception as e:
        print(e)

total_salary("./test1.txt")

# Task 2

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
    except Exception as e:
        print(e)
    finally:
        return b


# Task 3


import sys
from colorama import init, AnsiToWin32, Fore, Back, Style
init(wrap=True)
stream = AnsiToWin32(sys.stderr).stream

def rec(path, level = 0):

    folder = '\U0001F4C1'
    a = '\U00002516'
    b = '\U0001F4DC'
    
    directory = Path(path)
    
    for path in directory.iterdir():    
        if path.is_dir():
            level += 1
            if level == 1:
                print( f"{Fore.MAGENTA}{a}{folder}{path.name}{Style.RESET_ALL}",file=stream)
            if level > 1:
                print( f"{' ' * (level-1)*4}{Fore.CYAN}{Back.YELLOW}{a}{folder}{path.name}{Style.RESET_ALL}",file=stream)
            rec(path, level)
            level -= 1 
        if path.is_file():
            level += 1
            print( f"{' '*4*(level-1)}{Fore.GREEN}{Back.BLACK}{a}{Back.WHITE}{b}{Back.BLACK}{path.name}, ур {level}{Style.RESET_ALL}",file=stream)
                
rec(sys.argv[1])        

# Task 4

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    name, phone = args
    if name in contacts:
        return f"Contact {name} exists"
    else:
        contacts[name] = phone
        return "Contact added."

def change_contact(args, contacts):
    name, phone = args
    # contacts[name] = phone
    # print(contacts)
    if name in contacts:
        contacts[name] = phone
        return "Contact updated"
    else:
        return "Contact not found. Please, use command 'add'"

def show_phone(args, contacts):
    name = args[0]
    if name in contacts:
        return contacts[name]
    else:
        return "Contact not found."


def main():
    contacts = {}
    # a = contacts.items
    print("Welcome to the assistant bot!")
    try:
        while True:
            user_input = input("Enter a command: ")
            command, *args = parse_input(user_input)

            if command in ["close", "exit"]:
                print("Good bye!")
                break
            elif command == "hello":
                print("How can I help you?")
            elif command == "add":
                print(add_contact(args, contacts))
            elif command == "change":
                print(change_contact(args, contacts))
            elif command == "show":
                print(show_phone(args, contacts))
            elif command == "all":
                print(contacts)
            else:
                print("Invalid command.")
            # print(contacts)
    except Exception as e:
        print( e, "Введите корректную команду")
        
        # main()
    
    
    

if __name__ == "__main__":
    main()

