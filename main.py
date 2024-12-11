import random
import string

def generate_password(length=12):
    # Define the QWERTZ characters, numbers, and special characters
    qwertz_lower = "qwertzuiopasdfghjklyxcvbnm"
    qwertz_upper = qwertz_lower.upper()
    digits = string.digits  # "0123456789"
    special_chars = "!@#$%^&*()_+-=[]{}|;:',.<>?/"

    # Create a combined pool of characters
    all_characters = qwertz_lower + qwertz_upper + digits + special_chars

    # Generate a random password of specified length
    password = ''.join(random.choices(all_characters, k=length))

    return password

def main():
    while True:
        # Generate a random password and display it
        password = generate_password()
        print(f"Generated Password: {password}")

        # Ask the user if they want another password
        user_input = input("Generate another password? (Y/N): ").strip().upper()

        # Validate user input
        while user_input not in ('Y', 'N'):
            print("Invalid input. Please enter 'Y' for Yes or 'N' for No.")
            user_input = input("Generate another password? (Y/N): ").strip().upper()

        if user_input == 'N':
            print("Goodbye!")
            break



if __name__ == "__main__":
    main()
