import random
import string


# 1. Random Number
def random_number():
    num = random.randint(1, 100)
    print("Random Number:", num)


# 2. Random List
def random_list():
    numbers = random.sample(range(1, 50), 5)
    print("Random List:", numbers)


# 3. Random Password
def random_password():
    length = int(input("Enter password length: "))
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    password = ""
    for i in range(length):
        password = password + random.choice(characters)
    print("Generated Password:", password)


# 4. Random OTP
def random_otp():
    otp = random.randint(1000, 9999)
    print("Generated OTP:", otp)