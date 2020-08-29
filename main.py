# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import dirty_main

from datetime import datetime
from application.db import people

# Вариант 1
#from application import salary
# Вариант 2
import application.salary

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def main():

    print(f'Today is {datetime.today().date()}.')

    # Вариант 1
    #salary.calculate_salary()
    # Вариант 2
    application.salary.calculate_salary()
    people.get_employees()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
