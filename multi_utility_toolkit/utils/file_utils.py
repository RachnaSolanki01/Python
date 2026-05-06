#Create File
def create_file():
    file_name = input("Enter file name: ")
    file = open(file_name, "w")
    file.close()

    print("File Created Successfully.")


#Write File
def write_file():
    file_name=input("Enter file name: ")
    data = input("Enter data to write: ")
    file=open(file_name, "w")
    file.write(data)
    file.close()

    print("Data written Successfully.")


#Read File
def read_file():
    file_name=input("Enter file name: ")
    file=open(file_name, "r")
    content=file.read()
    file.close()

    print("File Content: ")
    print(content)


#Append File

def append_file():
    file_name=input("Enter file name: ")
    data=input("Enter data to append: ")
    file=open(file_name, "a")
    file.write("\n"+data)
    file.close()

    print("Data appended successfully!")