def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError as e:
            return f"Contact not found: {e.args[0]}"
        except IndexError:
            return "Invalid command. Please provide the required arguments."

    return inner


@input_error
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args



@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."


@input_error
def change_contact(args, contacts):
    if len(args) != 2:
        return "Invalid command. Please provide a name and a new phone number."

    name, new_phone = args
    contacts[name] = new_phone
    return "Contact updated."


@input_error
def show_phone(args, contacts):
    if len(args) != 1:
        return "Invalid command. Please provide a name."

    name = args[0]
    return contacts[name]


@input_error
def show_all(args, contacts):
    if args:
        return "Invalid command. 'all' command doesn't require additional arguments."

    if contacts:
        for name, phone in contacts.items():
            print(f"{name}: {phone}")
    else:
        return "No contacts found."


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Goodbye!")
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
            show_all(args, contacts)
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()