import datetime

#ShowCurrent DateTime
def show_current_datetime():
    current = datetime.datetime.now()
    print("Current Date and Time: ", current)


#DateDifference
def date_difference():
    date1= input("Enter first date(YYYY-MM-DD): ")
    date2= input("Enter second date(YYYY-MM-DD): ")

    d1=datetime.datetime.strptime(date1, "%Y-%m-%d")
    d2=datetime.datetime.strptime(date2, "%Y-%m-%d")

    difference = d2 - d1

    print("Difference in Days: ", abs(difference.days))


#FormatDate
def format_date():
    date_input = input("Enter date (YYYY-MM-DD): ")

    date_obj = datetime.datetime.strptime(date_input, "%Y-%m-%d")

    formatted=date_obj.strftime("%Y-%m-%d")

    print("Formatted Date: ", formatted)

import time


#Stopwatch
def stopwatch():
    input("Press Enter to start stopwatch...")
    start = time.time()

    input("Press Enter to stop stopwatch...")
    end=time.time()

    elapsed=end-start

    print("Time elapsed:", round(elapsed, 2), "Seconds")


#Countdown Timer

def countdown_timer():
    seconds=int(input("Enter number of seconds: "))

    while seconds > 0:
        print("Time remaining:", seconds, "Seconds")
        time.sleep(1)
        seconds-= 1

    print("Time is Up...!!!")