import re

def is_valid_ip(ip):
    """Validate if a string is valid IP address."""
    pattern = r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$"
    return re.match(pattern, ip) is not None

def read_valid_ips():
    """Read IPs from a file and print only the valid ones."""
    try:
        with open("ip_addresses.txt", "r") as file:
            lines = file.readlines()
            print ("\n=== Valid IP Addresses ===")
            for line in lines:
                ip = line.strip()
                if is_valid_ip(ip):
                    print(ip)
    except FileNotFoundError:
        print("The file 'ip_addresses.txt' was not found.")

def write_ip():
    """Append a new IP address to the file."""
    new_ip = input(" Enter an IP address to append to the file: ")
    if is_valid_ip(new_ip):
        with open("ip_addresses.txt", "a") as file:
            file.write(f"{new_ip}\n")
        print(f"Successfully added {new_ip} to the file.")
    else:
        print("Invlaid IP address format. Please try again.")

def ip_file_handler():
    """Menu for reading and writing IPs."""
    while True:
        print("\n=== IP File Handler ===")
        print("1. Read valid IP addresses")
        print("2. Append a new IP address")
        print("3. Back to main menu")

        choice = input("Slect an option (1-3): ")

        if choice == '1':
            read_valid_ips()
        elif choice == '2':
            write_ip()
        elif choice == '3':
            break
        else:
            print('Invlaid option. Please try again')

if __name__ == "__main__":
    ip_file_handler()

    