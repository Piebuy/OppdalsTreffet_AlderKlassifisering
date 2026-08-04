from auth_services import *

def main():
    print("---If you have never used this program before you need to register your NBF username and password--- \n" \
    "---Then you can log in and the program will fetch the data for you---")
    print()
    inp = input("What do you want to do? \n1. log in\n2. register username and password \n3. delete password? \n\nplease enter 1, 2 or 3: ")

    if inp not in ["1", "2", "3"]:
        inp = input("Invalid input. Please enter 1, 2 or 3: ")

    if inp == "1":
        username = input("\nEnter username: ")
        if login(username):
            return True,username.lower()
        else:
            print("Login failed.")
    elif inp == "2":
        username = input("Enter username: ")
        password = getpass.getpass("Enter password: ")
        password_repeat = getpass.getpass("Repeat password: ")
        if password != password_repeat:
            print("Passwords do not match. Please try again.")
        else:
            store_password(username, password)
    elif inp == "3":
        username = input("Enter username: ")
        if login(username):
            delete_password(username)
        else:
            print("Password deletion aborted due to failed login.")
    return False,None
