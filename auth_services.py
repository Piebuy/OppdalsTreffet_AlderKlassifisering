import keyring
from keyring.errors import PasswordDeleteError
import getpass

def store_password(username, password):
    keyring.set_password(
        "NBF",
        username.lower(),
        password
    )

    print("Password stored")

def delete_password(username):
    try:
        stored_password = keyring.get_password("NBF", username)
        if stored_password is None:
            print("No password found for the given username.")
            return
        else:
            keyring.delete_password("NBF", username)
    except PasswordDeleteError:
        print("Failed to delete password. Please check if the username is correct and try again.")
        return

    print("Password deleted")

def login(username):
    entered_password = getpass.getpass("Enter password: ")
    stored_password = keyring.get_password("NBF", username.lower())

    if entered_password == stored_password:
        print("\nAuthentication successful!")
        return True
    else:
        print("\nInvalid username or password.")
        return False

