from utils import datetime_utils, math_utils, random_utils, uuid_utils, file_utils, explore_utils

def main_menu():
    while True:
        print("""---Multi Utility Toolkit---
1. Datetime Operations.
2. Math Operations.
3. Random Module
4. UUID Generator
5. File Operations
6. Explore Module(dir)
7. Exit
""")

        choice = input("Enter the Choice: ")

        if choice == "1":
            while True:
                print("\n---Datetime Module---")
                print("1. Show Current Date & Time")
                print("2. Date Difference")
                print("3. Format Date")
                print("4. Stopwatch")
                print("5. Countdown Timer")
                print("6. Back to Main Menu")

                sub_choice = input("Enter your choice: ")
                
                if sub_choice == "1":
                    datetime_utils.show_current_datetime()
                elif sub_choice == "2":
                    datetime_utils.date_difference()
                elif sub_choice == "3":
                    datetime_utils.format_date()
                elif sub_choice == "4":
                    datetime_utils.stopwatch()
                elif sub_choice == "5":
                    datetime_utils.countdown_timer()
                elif sub_choice == "6":
                    break
                else:
                    print("Invalid Option")

        elif choice == "2":
            while True:
                print("\n--- Mathematical Operations ---")
                print("1. Calculate Factorial")
                print("2. Solve Compound Interest")
                print("3. Trigonometric Calculations")
                print("4. Area of Shapes")
                print("5. Back to Main Menu")
                
                sub_choice = input("Enter your choice: ")

                if sub_choice == "1":
                    math_utils.calculate_factorial()
                elif sub_choice == "2":
                    math_utils.compound_interest()
                elif sub_choice == "3":
                    math_utils.trigonometry()
                elif sub_choice == "4":
                    math_utils.area_of_shapes()
                elif sub_choice == "5":
                    break

        elif choice == "3":
            while True:
                print("\n--- Random Data Generation ---")
                print("1. Generate Random Number")
                print("2. Generate Random List")
                print("3. Create Random Password")
                print("4. Generate Random OTP")
                print("5. Back to Main Menu")

                sub_choice = input("Enter your choice: ")

                if sub_choice == "1":
                    random_utils.random_number()
                elif sub_choice == "2":
                    random_utils.random_list()
                elif sub_choice == "3":
                    random_utils.random_password()
                elif sub_choice == "4":
                    random_utils.random_otp()
                elif sub_choice == "5":
                    break
                else:
                    print("Invalid choice")
        
        elif choice == "4":
            while True:
                print("\n--Generate Unique Identifiers(UUID)---")
                print("1. Generate UUID")
                print("2. Back to Main Menu")

                sub_choice = input("Enter the choice: ")

                if sub_choice == "1":
                    uuid_utils.generate_uuid()
                elif sub_choice == "2":
                    break
                else:
                    print("Invalid Choice")

        elif choice == "5":
            while True:
                print("\n---File Operations---")
                print("1. Create a New File")
                print("2. Write to a File")
                print("3. Read from a File")
                print("4. Append to a File")
                print("5. Back to Main Menu")

                sub_choice = input("Enter you choice: ")

                if sub_choice == "1":
                    file_utils.create_file()
                elif sub_choice == "2":
                    file_utils.write_file()
                elif sub_choice == "3":
                    file_utils.read_file()
                elif sub_choice == "4":
                    file_utils.append_file()
                elif sub_choice == "5":
                    break
                else:
                    print("Invalid Choice")

        elif choice == "6":
            while True:
                print("\n---Module Exploration---")
                print("1. Explore Modules")
                print("2. Back to Main Menu")

                sub_choice = input("Enter your choice: ")

                if sub_choice == "1":
                    explore_utils.explore_module()

                elif sub_choice=="2":
                    break

                else:
                    print("Invalid Choice")


        elif choice== "7":
            print("Exiting Program...! GoodBye!!!")
            break

        else:
            print("Invalid Choice, try again!")

if __name__ == "__main__":
    main_menu()