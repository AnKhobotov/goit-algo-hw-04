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



