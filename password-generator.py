import random
import string

def generate_password(length):
    # Define character sets for different complexity levels
    lower_case = string.ascii_lowercase
    upper_case = string.ascii_uppercase
    digits = string.digits
    special_chars = string.punctuation

    # Combine character sets based on desired complexity
    all_chars = lower_case + upper_case + digits + special_chars

    # Generate password using random.choice
    password = ''.join(random.choice(all_chars) for _ in range(length))
    return password

def main():
    print("Welcome to Password Generator!")
    
    while True:
        try:
            length = int(input("Enter the desired length of the password: "))
            if length > 0:
                break
            else:
                print("Invalid length. Please enter a positive integer.")
        except ValueError:
            print("Invalid length. Please enter a positive integer.")

    password = generate_password(length)
    print("Your generated password is:", password)

if __name__ == "__main__":
    main()
