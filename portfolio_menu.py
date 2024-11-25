import sys
from password_checker.password_checker import check_password_strength
from vowel_counter import vowel_counter
from ip_file_handler import ip_file_handler
from login_system import login_system
from weather_report import weather_report
from regex_parser import extract_emails
from password_manager import store_password, verify_stored_passwords

def password_manager():
    """Run the password manager."""
    while True:
        print("\n== Password Manager ===")
        print("1. Store a password")
        print("2. Verify a password")
        print("3. Back to menu")
        choice = input("Select an option (1-3): ")
        if choice == "1":
            store_password()
        elif choice == "2":
            verify_stored_passwords()
        elif choice == "3":
            break





def regex_parser():
    """Run the email extractor"""
    extract_emails("sample_log.txt")

def show_greeting():
    """ Function to demonstrate basic syntax """
    print("\n=== Portfolio Greeter ===")
    name = input ("What us your name? ")
    print(f"Hello, {name}! This portfolio will showcase my Python Skills as I learn.")
    print("Check back soon as I add more projects!\n")

def portfolio_menu():
    """Main menu for the portfolio"""
    while True:
        print("\n=== Python Cybersecurity Portfolio ===")
        print("1. Basic Syntax - Portfolio Greeter")
        print("2. Control Flow - Password Checker")
        print("3. Functions - Vowel Counter")
        print("4. File Handling - IP Address Reader/Writer")
        print("5. Lists and Dictionaries - Login System")
        print("6. Modules and Libraries - Weather Report")
        print("7. Regular Expressions Email Extractor")
        print("8. Hashing Password - Password Manager")

        choice = input("\nSelect an option (1-8): ")

        if choice == '1':
            show_greeting()
        elif choice == '2':
            check_password_strength()
        elif choice == '3':
            vowel_counter()
        elif choice == '4':
            ip_file_handler()
        elif choice =='5':
            login_system()
        elif choice == '6':
            weather_report()
        elif choice == '7.':
            regex_parser()
        elif choice == '8':
            password_manager()        
        elif print("Exiting the Portfolio. Goodbye!"):
            sys.exit()
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    portfolio_menu()



