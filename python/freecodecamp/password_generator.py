import re
import secrets
import string


def generate_password(length=16, nums=1, special_chars=1, uppercase=1, lowercase=1):
    # nums, special_chars, uppercase, lowercase = minimum required of each type

    # Define the possible characters for the password
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation

    # Combine all characters
    all_characters = letters + digits + symbols

    while True: # keep generating until a password is valid (break = exit)
        password = ''
        # Generate password, draw `length` random characters, one at a time
        for _ in range(length):
            password += secrets.choice(all_characters)

        # (minimum required, pattern that matches ONE character of that type)
        # r'...' = raw string: keep the backslash for the regex engine
        constraints = [
            (nums, r'\d'),
            (special_chars, fr'[{symbols}]'),
            (uppercase, r'[A-Z]'),
            (lowercase, r'[a-z]')
        ]
        print(password)
        print(constraints)

        # Check constraints
        # re.findall(pattern, password) -> list of matching characters
        # len(...) -> how many were found
        # all(...) -> True only if EVERY constraint is satisfied      
        if all(
            constraint <= len(re.findall(pattern, password))
            for constraint, pattern in constraints
        ):
            break # valid password: leave the loop
    
    return password

# __name__ is '__main__' only when this file is run directly
# (not when it is imported from another file)
if __name__ == '__main__':
    new_password = generate_password()
    print('Generated password:', new_password)