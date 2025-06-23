def parse_input(user_input: str) -> tuple[str, list[str]]:
    """
    Parse user input into command and arguments.
    
    Args:
        user_input (str): The raw input string from the user.
        
    Returns:
        tuple[str, list[str]]: A tuple containing the command and a list of arguments.
    """
    # Handle empty input
    if not user_input.strip():
        return "", []
        
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args

def add_contact(args: list[str], contacts: dict[str, str]) -> str:
    """
    Add a new contact to the contacts dictionary.
    
    Args:
        args (list[str]): List containing name and phone number.
        contacts (dict[str, str]): Dictionary of contacts with names as keys and phone numbers as values.
        
    Returns:
        str: Status message.
    """
    if len(args) != 2:
        return "Error: Invalid number of arguments. Usage: add [name] [phone]"
    
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def change_contact(args: list[str], contacts: dict[str, str]) -> str:
    """
    Change the phone number of an existing contact.
    
    Args:
        args (list[str]): List containing name and new phone number.
        contacts (dict[str, str]): Dictionary of contacts with names as keys and phone numbers as values.
        
    Returns:
        str: Status message.
    """
    if len(args) != 2:
        return "Error: Invalid number of arguments. Usage: change [name] [new phone]"
    
    name, phone = args
    
    if name not in contacts:
        return f"Error: Contact '{name}' not found."
    
    contacts[name] = phone
    return "Contact updated."

def show_phone(args: list[str], contacts: dict[str, str]) -> str:
    """
    Show the phone number of a specific contact.
    
    Args:
        args (list[str]): List containing the name of the contact.
        contacts (dict[str, str]): Dictionary of contacts with names as keys and phone numbers as values.
        
    Returns:
        str: The phone number or an error message.
    """
    if len(args) != 1:
        return "Error: Invalid number of arguments. Usage: phone [name]"
    
    name = args[0]
    
    if name not in contacts:
        return f"Error: Contact '{name}' not found."
    
    return contacts[name]

def show_all(args: list[str], contacts: dict[str, str]) -> str:
    """
    Show all contacts and their phone numbers.
    
    Args:
        args (list[str]): Should be empty.
        contacts (dict[str, str]): Dictionary of contacts with names as keys and phone numbers as values.
        
    Returns:
        str: Formatted string of all contacts or an error message.
    """
    if args:
        return "Error: This command doesn't take any arguments. Usage: all"
    
    if not contacts:
        return "No contacts saved."
    
    result = []
    for name, phone in contacts.items():
        result.append(f"{name}: {phone}")
    
    return "\n".join(result)

def main() -> None:
    """Main function that runs the assistant bot."""
    contacts = {}
    print("Welcome to the assistant bot!")
    
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)
        
        match command:
            case "close" | "exit":
                print("Good bye!")
                break
                
            case "hello":
                print("How can I help you?")
                
            case "add":
                print(add_contact(args, contacts))
                
            case "change":
                print(change_contact(args, contacts))
                
            case "phone":
                print(show_phone(args, contacts))
                
            case "all":
                print(show_all(args, contacts))
                
            case "":
                continue  # Skip empty inputs
                
            case _:
                print("Invalid command.")

if __name__ == "__main__":
    main()
