from datetime import datetime
print (f"Welcome to the Interactive Personal Data Collector")
Name= (input("Please enter your name: "))
Age= int(input("Please enter your age: "))
Height= float(input("Please enter your height in meters: "))
Number= int(input("Please enter your favorite number: "))
print (f" Thank you! Here is the information we collected: ")
print (f" Name: {Name} (type: {type(Name)}, Memory Address: {id(Name)})")
print (f" Age: {Age} (type: {type(Age)}, Memory Address: {id(Age)})")
print (f" Height: {Height} (type: {type(Height)}, Memory Address: {id(Height)})")
print (f" Favourite Number:{Number} (type: {type(Number)}, Memory Address: {id(Number)})")

datetime=datetime.now().year
birthyear=datetime-Age
print (f"Your birth year is approximaterly: {birthyear} (based on your age of {Age})")
print (f"Thank you for using the Personal Data Collector. Goodbye!")