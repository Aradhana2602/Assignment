import os
import sys

def prompt_exit():
    """Function to prompt the user to either continue or exit"""
    user_input = input("Press Enter to continue, or 'c' to exit...")
    if user_input.lower() == 'c':
        print("Exiting...")
        sys.exit()

def main():
    while True:
        # Display the options to the user
        print("What would you like to do? (Enter the number)\n")
        print("1. Create an admin")
        print("2. Add communities and rules to the database")
        print("3. Add rules to communities")
        print("4. Add moderators to communities (also available from the admin panel)")
        print("5. Remove moderators from communities (also available from the admin panel)\n")
        print("Press 'c' and Enter to exit or any other key to continue...")

        # Get user input
        choice = input().strip()

        # Handle the choices
        if choice == '1':
            os.system('node "scripts/create-admin.js"')
            prompt_exit()
        elif choice == '2':
            os.system('node "scripts/add-community.js"')
            prompt_exit()
        elif choice == '3':
            os.system('node "scripts/add-rules.js"')
            prompt_exit()
        elif choice == '4':
            os.system('node "scripts/add-moderator.js"')
            prompt_exit()
        elif choice == '5':
            os.system('node "scripts/remove-moderator.js"')
            prompt_exit()
        elif choice.lower() == 'c':
            print("Exiting...")
            sys.exit()
        else:
            print("Invalid input, please try again.")

if __name__ == "__main__":
    main()
