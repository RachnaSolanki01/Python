while(True):
    print("Select an option:")
    print (f"1.Generate a Pattern")
    print (f"2.Generate a Range of Numbers")
    print(f"3.Exit")
    Choice=int(input("Enter your choice: "))
    match Choice:
        case 1:
            i=int(input("Enter your choice: "))
            j=int(input("Enter the number of rows for the pattern: "))
            for i in range(i,j):
                for j in range(i):
                    print("*", end="")
                print()
        case 2:
            s=int(input("Enter the Start of the range: "))
            e=int(input("Enter the end of the range: "))
            add=0
            for i in range(s,e):
                if i % 2 == 0:
                    print(f"Number {i} is Even")
                else:
                    print(f"Number {i} is odd")
                add+=i
            print(f"Sum of all number from {s} to {e-1} is {add}")
        case 3:
            print("Exiting the program. Good Bye!")
            break