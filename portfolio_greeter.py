import json

def greet_user():
    name = input("Welcome to my Python portfolio! What is your name? ")
    age = int(input("How old are you?"))

    if age < 18:
        print(f"Hello, {name}! You're quite young to be learning Python!")
    else:
        print(f"Hello, {name}! It's never too late to learn python!")

    user_data = {"name": name, "age": age}
    with open("user_data.json", "w") as f:
        json.dump(user_data, f)

if __name__ == "__main__":
    greet_user()            
    