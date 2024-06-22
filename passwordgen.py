import random
import string
def gen_pass(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password_list = random.choices(characters, k=length)
    password = ''.join(password_list)
    return password


def main():
    while True:
        try:
            length = int(input("Enter the required length for the password: "))

            if length < 1:
                print("Password length must be at least 1")
                continue
            password = gen_pass(length)
            print("Generated password:", password)
        except ValueError:
            print("Invalid input. Please enter a valid integer for the password length.")

        ch = input("Do you want to generate another password? (yes/no): ").lower()
        if ch != 'y':
            print("Thank you for using the password generator.")
            break


if __name__ == "__main__":
    main()
