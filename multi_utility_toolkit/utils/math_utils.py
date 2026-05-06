import math

#Calculate Factorial
def calculate_factorial():
    num = int(input("Enter a Number: "))
    result=math.factorial(num)

    print("Factorial: ", result)


#Compound Interest
def compound_interest():
    principal = float(input("Enter principal amount: "))
    rate = float(input("Enter rate of interest (in %): "))
    time = float(input("Enter time (in years): "))

    amount = principal * (1 + rate/100) ** time

    print("Compound Interest:", round(amount, 2))


#Trigonometric
def trigonometry():
    import math

    angle=float(input("Enter angle in degrees: "))

    radians=math.radians(angle)

    print("sin:", round(math.sin(radians), 2))
    print("cos:", round(math.cos(radians), 2))
    print("tan:", round(math.tan(radians), 2))


#Area of Shapes
def area_of_shapes():
    import math

    print("\nChoose Shape:")
    print("1. Circle")
    print("2. Square")
    print("3. Triangle")

    choice=input("Enter your choice: ")

    if choice == "1":
        radius = float(input("Enter Radius: "))
        area = math.pi * radius * radius
        print("Area of Circle: ", round(area, 2))

    elif choice == "2":
        side = float(input("Enter Side: "))
        area = side * side
        print("Area of Square: ", area)

    elif choice == "3":
        base = float(input("Enter base: "))
        height = float(input("Enter height: "))
        area = 0.5 * base * height
        print("Area of Triangle: ", area)

    else:
        print("Invalid Choice")