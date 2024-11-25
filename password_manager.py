import bcrypt

def hash_password(password):
    """Hash a password using bcrypt"""
    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    return hashed

def verify_password(hashed_password, user_password):
    """Verify a password against it's hash."""
    return bcrypt.checkpw(user_password.encode(), hashed_password)

def store_password():
    """Store a hashed password in a file."""
    password = input("Enter a password to hash and store: ")
    hashed = hash_password(password)
    with open("passwords.txt", "ab") as file:
        file.write(hashed + b"\n")
    print("Password hashed and stored.")

def verify_stored_passwords():
    """Verify user input against stored hash passwords."""
    user_password = input("Enter the password to verify: ")
    try:
        with open("passwords.txt", "rb") as file:
            for line in file:
                hashed = line.strip()
                if verify_password(hashed, user_password):
                    print("Password Match!")
                    return
        print("No matching password found")
    except FileNotFoundError:
        print("NO passwords stored yet.")

if __name__ == "__main__":
    while True:
        print("\n=== Password Manager ===")
        print("1. Store a password")
        print("2. Verify a password")
        print("3. Exit")
        choice = input("select and option (1-3): ")
        if choice == "1":
            store_password()
        elif choice == "2":
            verify_stored_passwords()
        elif choice == "3":
            break
        else:
            print("Invalid option. Please try again.")


            

    
