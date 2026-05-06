import math
import random
import datetime


def explore_module():
    print("\nChoose Module:")
    print("1. Math")
    print("2. Random")
    print("3. Datetime")


    choice = input("Enter your choice: ")

    if choice == "1":
        print(dir(math))

    elif choice == "2":
        print(dir(random))
    
    elif choice == "3":
        print(dir(datetime))

    else:
        print("Invalid Choice")
