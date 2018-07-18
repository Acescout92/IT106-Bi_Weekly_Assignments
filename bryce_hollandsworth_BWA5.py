#-------------------------------------------------------------------------------
# bryce_hollandsworth_BWA5.py
# Student Name:  Bryce
# Python version: Hollandsworth
# Submission Date: 04/19/2018
#-------------------------------------------------------------------------------
# Honor Code Statement: I received no assistance on this assignment that
# violates the ethical guidelines as set forth by the
# instructor and the class syllabus.
#-------------------------------------------------------------------------------
# References: 
#-------------------------------------------------------------------------------
# Notes to grader: 
#-------------------------------------------------------------------------------
# NOTE: width of source code should be < 80 characters to facilitate printing
#-------------------------------------------------------------------------------

def main():
    """Implements main menu. Opens then overwrites target file"""
    rolo = {}
    with open('rolodex.txt', 'r') as rolodex:
        for val in rolodex.readlines():
            splited = val.split()
            splited[1] = splited[1].split(',')
            rolo[splited[0]] = splited[1]
    main_menu = int(input("Welcome to the main menu.\n1.Display Entry\n2.Add Entry\n3.Delete Entry\n4.Display Rolodex\n5.Exit"))
    while main_menu != 5:
        if main_menu == 1:
            display_entry(rolo)
            main_menu = int(input("Welcome to the main menu.\n1.Display Entry\n2.Add Entry\n3.Delete Entry\n4.Display Rolodex\n5.Exit"))
        elif main_menu == 2:
            rolo = add_entry(rolo)
            main_menu = int(input("Welcome to the main menu.\n1.Display Entry\n2.Add Entry\n3.Delete Entry\n4.Display Rolodex\n5.Exit"))
        elif main_menu == 3:
            rolo = delete_entry(rolo)
            main_menu = int(input("Welcome to the main menu.\n1.Display Entry\n2.Add Entry\n3.Delete Entry\n4.Display Rolodex\n5.Exit"))
        elif main_menu == 4:
            display_rolodex(rolo)
            main_menu = int(input("Welcome to the main menu.\n1.Display Entry\n2.Add Entry\n3.Delete Entry\n4.Display Rolodex\n5.Exit"))
    with open('rolodex.txt', 'w') as new_rolo:
        for val, val2 in rolo.items():
            name = val + " " + val2[0] 
            number = str(val2[1])
            final = name + ', ' + number
            new_rolo.write(final)
            

def display_entry(rolo):
    """Displays the information of targeted person"""
    n = input("Please input desired name, or q to return to main: ")
    while n !='q':
        if n in rolo.keys():
            print(rolo[n])
            n = input("Please input desired name, or q to return to the main menu\n")
        else:
            print("Name does not exist in database.")
            n = input("Please input desired name, or q to return to the main menu\n")

def add_entry(rolo):
    """Accepts new user info"""
    n = input("Please enter the first name you would like to add to the database, or press q to return to main: ")
    while n != 'q':
        last = input("Please input last name for: " + n)
        phone = int(input("Please input the phone number without dashes: "))
        rolo[n] = [last, phone]
        n = input("Please enter the first name you would like to add to the database, or press q to return to main: ")
    return rolo

def delete_entry(rolo):
    """Deletes target key"""
    n = input("Enter the first name of the user that you would like to delete, or press q to return to main menu\n")
    while n!='q':
        if n in rolo.keys():
            del rolo[n]
            n = input("Enter the first name of the user that you would like to delete, or press q to return to main menu\n")
        else:
            print("User not found. ")
            n = input("Enter the first name of the user that you would like to delete, or press q to return to main menu\n")
    return rolo

def display_rolodex(rolo):
    """Displays all items in the rolodex"""
    for val, val2 in rolo.items():
        print(val, val2)
    
main()