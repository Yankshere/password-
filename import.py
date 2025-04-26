import random 
import string

def generate_password(length, use_special_chars, use_numbers, use_uppercase, use_lowercase, use_digits ):
    characters = ''
    if use_special_chars:
        characters += string.punctuation
        if use_numbers:
            characters += string.digits
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if not characters:
        raise ValueError("At least one character type must be selected")
    categories = [
        random.choice(string.ascii_uppercase),
        random.choice(string.ascii_lowercase),
        random.choice(string.digits),
        random.choice(string.punctuation)
    ]

    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password



if __name__ == "__main__":
    length = int(input("Enter the desired password length: "))
    use_special_chars = input("Include special characters? (y/n): ").lower() == 'y'
    use_numbers = input("Include numbers? (y/n): ").lower() == 'y'
    use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
    use_digits = input("Include digits? (y/n): ").lower() == 'y'

    password = generate_password(length, use_special_chars, use_numbers, use_uppercase, use_lowercase, use_digits)
    print(f"Generated password: {password}")