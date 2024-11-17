import sys
from password_checker.password_checker import check_password_strength
from vowel_counter import vowel_counter
from ip_file_handler import ip_file_handler
from login_system import login_system
from weather_report import weather_report

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
        print("7. Exit")

        choice = input("\nSelect an option (1-4): ")

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
        elif choice == '7':
            print("Exiting the Portfolio. Goodbye!")
            sys.exit()
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    portfolio_menu()



