import random

ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
digits = '0123456789'
special_characters = '!@#$%^&*?'
all_characters = ascii_lowercase + ascii_uppercase + digits + special_characters


def password_generator():
    while True:
        password_length = int(input("Enter a length of password: "))
        if password_length < 8:
            print("Password must 8 characters")
            continue
        else:
            password = ''
            for i in range(password_length):
                password_choices = random.choice(all_characters)
                password += password_choices
            return password


print(f"Your password is : {password_generator()}")
