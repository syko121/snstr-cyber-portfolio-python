import hashlib

# A dictionary to store users and their hashed passsword
users = {
    "admin": hashlib.sha256("admin123".encode()).hexdigest(),
    "user1": hashlib.sha256("password1".encode()).hexdigest(),
    "user2": hashlib.sha256("password2".encode()).hexdigest(),
}

# A list to track login attempts
login_attempts = []

def hash_password(password):
    """Has a password using SHA-256."""
    return hashlib.sha256(password.encode()).hexdigest()

def check_login(username, password):
    """ Check teh login credntials and return True for success or False for failure."""
    hashed_password = hash_password(password)
    if username in users and users[username] == hashed_password:
        return True
    return False

def login_system():
    """Simulated login system with login attempt tracking."""
    while True:
        print("\n=== Login System ===")
        username = input("Username: ")
        password = input("Password: ")

        if check_login(username, password):
            print ("Login Successful!")
            login_attempts.append((username, "Success"))
        else:
            print("Login failed.")
            login_attempts.append((username, "Failure"))
        
        choice = input("\nDo you want to try again (y/n) or view the login log (log)? ")

        if choice.lower() == 'n':
            break
        elif choice.lower() == 'log':
            view_log()

def view_log():
    """View the log of login attempts."""
    print("\n=== Login Attempts log ===")
    for attempt in login_attempts:
        print(f"User: {attempt[0]}, Status: {attempt[1]}")

if __name__ == "__main__":
    login_system()
