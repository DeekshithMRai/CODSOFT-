import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def main():
    while True:
        try:
            length = int(input("Enter the desired password length: "))
            if length < 1:
                raise ValueError("Password length must be greater than 0")
            break
        except ValueError as e:
            print(e)
    
    password = generate_password(length)
    
    print(f"Generated password is : {password}")

if __name__ == "__main__":
    main()
