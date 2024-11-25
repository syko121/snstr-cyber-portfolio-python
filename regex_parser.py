import re

def extract_emails(file_path):
    """Extract all valid email address from a file.""" 
    try:
        with open(file_path, "r") as file:
            content = file.read()
            # Regex for finding email addresses
            email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
            emails = re.findall(email_pattern, content)
            for email in emails:
                print(email)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")

if __name__ == "__main__":
    extract_emails("sample_log.txt")
