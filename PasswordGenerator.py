import random
import string

def generate_password(length, include_digits=True, include_special=True):
    # Define the character sets to use in generating the password
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits if include_digits else ''
    special_characters = '@$%&*' + string.punctuation if include_special else ''
    
    # Combine all character sets
    all_characters = lowercase_letters + uppercase_letters + digits + special_characters
    
    # Generate password using random.choice to ensure randomness
    password = ''.join(random.choice(all_characters) for _ in range(length))
    
    return password

def main():
    print("Welcome to the Password Generator!")
    
    while True:
        try:
            length = int(input("Enter the desired length of the password: "))
            if length <= 0:
                raise ValueError("Length must be a positive integer.")
            break
        except ValueError as e:
            print(f"Error: {e}. Please enter a valid positive integer.")
    
    include_digits = input("Include digits in the password? (yes/no): ").lower() in ['yes', 'y']
    include_special = input("Include special characters in the password? (yes/no): ").lower() in ['yes', 'y']

    generated_password = generate_password(length, include_digits, include_special)
    
    print(f"\nGenerated Password: {generated_password}")

if __name__ == "__main__":
    main()
