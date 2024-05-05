
def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (TypeError, ValueError):
            print("Enter the argument for the command")
        except (IndexError, KeyError):
            print("The contact not found.")
        except Exception as e:
            print(e)
                
    return inner


@input_error
def add_contact(args: str, contacts: dict) -> dict:
    """
    add new contact to contacts
    """
    name, phone = args
    if name not in contacts.keys():
        contacts[name] = phone
        print("Contact added.")
    else:
        raise Exception("The contact with name " + name + " already exists; phone: " + contacts[name])
    
    return contacts


@input_error
def change_contact(args: str, contacts: dict) -> dict:
    """
    change phone number for existing contact in contacts
    """
    name, phone = args
    contacts[name] = phone
    print("Contact updated.")
    
    return contacts
 

@input_error
def show_phone(args: str, contacts: dict) -> None:
    """
    show phone number for existing contact in contacts
    """
    name = args[0]
    print(contacts[name])    

