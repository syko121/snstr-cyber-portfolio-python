import sys
from password_checker import check_password_strength

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
        print("3. (Future Feature) Functions")
        print("4. Exit")

        choice = input("\nSelect an option (1-4): ")

        if choice == '1':
            show_greeting()
        elif choice == '2':
            check_password_strength()
        elif choice == '3':
            print("Function will be available soon!")
        elif choice == '4':
            print("Exiting the Porfolio. Goodbye!")
            sys.exit()
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    portfolio_menu()



