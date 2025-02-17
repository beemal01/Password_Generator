import random
import string

def welcome():
    print("Welcome to the password generator program....")

def pass_generator():
    letters = int(input("Enter how many letter you want in password : "))
    numbers = int(input("Enter how many number you want in password : "))
    characters = int(input("Enter how many special character you want in password : "))

    password = []

    for _ in range(1, int(letters)+1):
        password += random.choice(string.ascii_letters)

    for _ in range(1, numbers + 1):
        password += random.choice(string.digits)

    for _ in range(1, int(characters)+1):
        password += random.choice(string.punctuation)

    random.shuffle(password)
    password = ''.join(password)
    return password

welcome()
print(pass_generator())


while True:
    play = input("Enter 'play' to start generating password or 'end' for exit. : ").lower()
    if play == 'play':
        print(pass_generator())
    elif play == 'end':
        print("Thanks for choosing the password generator....")
        break
    else:
        print("Please enter correct option....")



