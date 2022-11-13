print()
print("*********Programmed by:*********")
print("*********Lyza Jorella R. Del Rosario*********")

My_Information = {}

while True:
    print()
    print("========================================")
    print()
    print("*******Add an item********")
    print("*******Search*******")
    print("*******Exit (y/n)*******")
    print()
    print("========================================")
    print()
    break

    # print the choices
n = int(input("What do you want to do?(1-2:)"))
if n == 1:
    My_Name = input("Full name:")
    My_Age = int(input("Age:"))
    My_Address = input("Address: ")
    My_Birthdate = input("Birthdate:")
    My_BirthPlace = input("BirthPlace: ")
    My_Contactnumber = int(input("Contactnumber:"))
    My_Citizenship = input("Citizenship: ")
    My_Religion = input("Religion: ")
    My_Information[My_Name] = {"Age:": My_Age, "Address:": My_Address, "Birthdate:": My_Birthdate,
                               "BirthPlace:": My_BirthPlace, "Contactnumber:": My_Contactnumber,
                               "Citizenship:": My_Citizenship, "Religion:": My_Religion}
    print("The information is saved!!!")

elif n == 2:
    My_Search = input("Search for full name: ")
    if My_Search in My_Information:
        for key, value in My_Information[My_Search].items():
            print(key, value)

        else:
            print(" Does not exist. )


