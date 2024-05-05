"""
Bot-helper, works with user contacts
"""

from parse import parse_input
from handler import add_contact, change_contact, show_phone


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command:").strip().lower()
        command, *args = parse_input(user_input)        
        
        if command in ["close", "exit"]:

            print("Good Bye!")
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            result = add_contact(args, contacts)
            if type(result) == dict:
                contacts.update(result)            
   
        elif command == "change":
            result = change_contact(args, contacts)
            if type(result) == dict:
                contacts.update(result)
        
        elif command == "phone":
            show_phone(args, contacts)
           
        elif command == "all":
            print(contacts)
        
        else:
            print("Invalid command.")
    
  
if __name__ == "__main__":
    main()




