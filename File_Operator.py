class JournalManager:

    def __init__(self):
        self.filename="journal.txt"

    def add_entry(self):
        entry=input("Enter your Note: ")
        
        from datetime import datetime
        time=datetime.now()

        try:
            file=open(self.filename, "a")
            file.write (str(time) + " - " + entry + "\n")
            file.close()

            print("Entry Saved")

        except:
            print("Something went Wrong")
#Add Entry

    def view_enteries(self):
        try:
            file=open(self.filename, "r")
            data=file.read()
            print("\nYour Entries:\n")
            print(data)
            file.close()

        except:
            print("No Entries found or file does not exist")
#View Entry

    def search_entry(self):
        word=input("Enter word to Search: ")

        try:
            file=open(self.filename, "r")

            found = False

            for line in file:
                if word in line:
                    print(line)
                    found = True

            if found == False:
                print("No matching entry found for keyword: " + word)

            file.close()

        except:
            print("File not found")
#Search Entry

    def delete_entries(self):
        confirm=input("Are you sure you want to delete all enteries?(Yes/No): ")

        if confirm=="Yes":
            try:
                file=open(self.filename, "w")
                file.write("")
                file.close()

                print("All entries deleted")

            except:
                print("Error while deleting")
        
        else:
            print("Deleted Cancelled")
#Delete Entry

def menu():
    print("""Welcome to Personal Journal Manager---
          1. Add a New Entry
          2. View All Enteries
          3. Search for an Entry
          4. Delete All Entries
          5. Exit"""
)
jm=JournalManager()

while True:
    menu()
    choice = input("Enter your choice: ")

    if choice=="1":
        jm.add_entry()

    elif choice=="2":
        jm.view_enteries()

    elif choice=="3":
        jm.search_entry()

    elif choice=="4":
        jm.delete_entries()

    elif choice=="5":
        print("Thank You for using Personal Journal Manager. GoodBye!")

    else:
        print("Invalid Choice. Please select a Valid Option.")

        break