#-------------------------------------------------------------------------------
# bryce_hollandsworth_bwa4.py
# Student Name: Bryce Hollandsworth
# Python version: 3.6
# Submission Date: 04/05/2018
#-------------------------------------------------------------------------------
# Honor Code Statement: I received no assistance on this assignment that
# violates the ethical guidelines as set forth by the
# instructor and the class syllabus.
#-------------------------------------------------------------------------------
# References: 
#-------------------------------------------------------------------------------
# Notes to grader: 
#------------------------------------------------------------------------------------------------
# NOTE: width of source code should be < 80 characters to facilitate printing
#-------------------------------------------------------------------------------
import os
import math
import time
def main_menu():
    """Main Menu. User input determines which function called"""
    selection = int(input("Please choose from the following\
                    \n1.Cylinder\n2.Cubes\n3.Spheres\n"))
    if selection == 1:
        print(cylinder_menu())
    elif selection == 2:
        print(cube_menu())
    elif selection == 3:
        print(sphere_menu())
    else:
        print("Invalid input, goodbye...")
        exit()

def cylinder_menu():
    """Menu for determining cylinder formulas"""
    while True:
        clear_screen()
        print("Welcome to the menu for cylinder formulas. Please choose the following: \n")
        choice = int(input("1.Volume\n2.lateral surface area\n"
        "3.Top and bottom surface area\n4.Total surface area\n"))
        clear_screen()
        radius = float(input("Input radius: "))
        height = float(input("input height: "))
        L = 2*math.pi*radius*height
        T = math.pi*radius**2
        clear_screen()
        if choice == 1:
            volume = math.pi*radius**2*height
            return volume
        elif choice == 2:
            return L
        elif choice == 3:
            return T
        elif choice == 4:
            A = L + T*2
            return A
        else:
            print("invalid menu choice, please try again\n")
            time.sleep(2)
            continue
def cube_menu():
    """Menu for cube formulas"""
    while True:
        clear_screen()
        print("Welcome to the cube formulas menu! Please choose from below:\n")
        choice = int(input("1.Volume\n2.Surface Area\n3.Face Diagonal\n"))
        clear_screen()
        side_length = float(input("Input length of cube side length: "))
        if choice == 1:
            volume = side_length**3
            return volume
        elif choice == 2:
            surface_area = 6*side_length**2
            return surface_area
        elif choice == 3:
            face_diagonal = side_length*math.sqrt(2)
            return face_diagonal
        else:
            print("Invalid menu choice, please try again...")
            time.sleep(2)
            continue

def sphere_menu():
    """Menu for sphere formulas"""
    while True:
        clear_screen()
        print("Now imagine the cow is a sphere....\n")
        choice = int(input("1.Volume\n2.Circumference\n3.Surface Area\n"))
        clear_screen()
        radius = float(input("Input radius: "))
        if choice == 1:
            volume = (4/3) * math.pi * radius**3
            return volume
        elif choice == 2:
            circumference = 2 * math.pi * radius
            return circumference
        elif choice == 3:
            surface_area = 4 * math.pi * radius**2
            return surface_area
        else:
            print("Invalid menu choice, please try again....")
            time.sleep(2)
            continue

def clear_screen():
    """clears screen when called"""
    if os.name == "nt":
        os.system('cls')
    else:
        os.system('clear')

main_menu()
