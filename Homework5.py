def parse_input(user_input):
    """
    Функція розбиває введений рядок на команду та аргументи.
    Використовується для парсингу введених команд користувача.
    """
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args

def add_contact(args, contacts):
    """
    Функція додає новий контакт до словника contacts.
    args має бути списком з ім'ям та номером телефону.
    """
    if len(args) != 2:
        return "Invalid command. Format: add [ім'я] [номер телефону]"
    
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def change_contact(args, contacts):
    """
    Функція змінює існуючий номер телефону для вказаного контакту.
    args має бути списком з ім'ям та новим номером телефону.
    """
    if len(args) != 2:
        return "Invalid command. Format: change [ім'я] [новий номер телефону]"
    
    name, new_phone = args
    if name in contacts:
        contacts[name] = new_phone
        return "Contact updated."
    else:
        return f"Contact '{name}' not found."

def show_phone(args, contacts):
    """
    Функція виводить номер телефону для вказаного контакту.
    args має бути списком з ім'ям контакту.
    """
    if len(args) != 1:
        return "Invalid command. Format: phone [ім'я]"
    
    name = args[0]
    if name in contacts:
        return contacts[name]
    else:
        return f"Contact '{name}' not found."

def show_all(contacts):
    """
    Функція виводить усі збережені контакти разом з номерами телефонів.
    """
    if not contacts:
        return "No contacts found."
    
    all_contacts = "\n".join(f"{name}: {contacts[name]}" for name in sorted(contacts))
    return all_contacts

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        
        elif command == "hello":
            print("How can I help you?")
        
        elif command == "add":
            print(add_contact(args, contacts))
        
        elif command == "change":
            print(change_contact(args, contacts))
        
        elif command == "phone":
            print(show_phone(args, contacts))
        
        elif command == "all":
            print(show_all(contacts))
        
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
