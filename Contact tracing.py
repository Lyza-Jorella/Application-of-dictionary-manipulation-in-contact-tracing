print()
print("********Programmed by:********")
print("********Lyza Jorella R. Del Rosario********")

My_Information = {}

while True:
    print()
    print("==================MENU==================")
    print()
    print("******(1)Add an item*******")
    print("******(2) Search******")
    print("******(3) Exit (y/n)******")
    print()
    print("========================================")
    print()

# print the choices
    n = int(input("What do you want to do?(1-3:)"))
    if n == 1:
        My_Name = input("Full name:")
        My_Age = int(input("Age:"))
        My_Address = input("Address: ")
        My_Birthdate = input("Birthdate:")
        My_BirthPlace = input("BirthPlace: ")
        My_Contact = int(input("Contact number:"))
        My_Citizenship = input("Citizenship: ")
        My_Religion = input("Religion: ")
        My_Information[My_Name] = {"Age:": My_Age, "Address:": My_Address, "Birthdate:": My_Birthdate,
                                   "BirthPlace:": My_BirthPlace, "Contactnumber:": My_Contact,
                                   "Citizenship:": My_Citizenship, "Religion:": My_Religion}
        print("The information is saved!!!")

    elif n == 2:
        My_Search = input("Search for full name: ")
        if My_Search in My_Information:
            for key, value in My_Information[My_Search].items():
                print(key, value)

        else:
            print(" Does not exist. ")

    elif n == 3:
        exit()
        break
    else:
        print("That is not a valid option.)
