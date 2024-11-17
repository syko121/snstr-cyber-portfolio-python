import re

def check_password_strength():
    """Check if password is strong based on length, digits, and special characters."""
    password = input("Enter a password to check it's strength:")

    if len(password) < 8:
        print("Password is too short. It should be 8 characters long.")
    elif not re.search(r"\d", password):
        print("Password should contain at least one digit.")
    elif not re.search(r"[!@#$%^&*()_+]", password):
        print ("Password should conatin at least one special character.")
    else:
        print("Password is strong!")

if __name__ == "__main__":
    check_password_strength()

