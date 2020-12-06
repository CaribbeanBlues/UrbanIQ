#################################################################################
"""
Youba Ltd. is a startup company that aims to revolutionize the local public transportation by
introducing a brand new way for travellers to connect with drivers. Users only need
to have a cellphone to utilize the service. Given your knowledge of ADTs, Youba Ltd.
has contracted you to implement the platform for their service.
"""

import os
import sys
import csv
from Library import *
import csv_access

#Databases
DEST_DB = 'database/destinations_database.csv'
NUM_DB = 'database/numbers_database.csv'
DRV_DB = 'database/driver_database.csv'


# dest_db = 'database/destinations_database.csv'
# num_db = 'database/numbers_database.csv'
queue_dict = {}
# with open(dest_db) as f:
#     reader = csv.reader(f)
#     header_row = next(reader)
#     destinations = []
#     for row in reader:
#         destinations.append(row[1])
# with open(num_db) as f:
#     reader = csv.reader(f)
#     header_row = next(reader)
#     numbers = {}
#     for row in reader:
#         numbers[row[0]] = row[1]
#
#
# def make_av_queues():
#     for destination in destinations:
#         queue_dict[destination] = queue.make_availability_queue(destination)
#     return queue_dict
#
#
# def add_to_av_queues(a_queue_list):
#     return make_av_queues()
#
# def add_destination(loc):
#     with open(destination, 'a') as f:
#         f.write(loc)



# TODO Make each section its own .py file
# TODO Run Pycharm's code analyzer

#################################################################################
# Main Section
#################################################################################


if __name__ == '__main__':
    lines = "********************************************************************"
    print(lines)
    print("*   Welcome to the Admin side.")
    print(strings.main_menu)
    while True:
        entry = int(input())
        if entry == 1:
            print(strings.driver_menu)
            entry = int(input())
            if entry == 1:
                print(strings.all_drivers_format)
                print(csv_access.get_all_items(DRV_DB))
                print(strings.continue_prompt)
                input()
            if entry == 2:
                edit = input(strings.edit_driver_prompt)
                if edit != 0:
                    old_driver = csv_access.get_item(edit)


        # Makes new Availability Queues

        # A list of queues
        a_queue_list = make_av_queues()  # TODO Generate a list of Availability Queues
        # A dictionary of customers and their failed attempts
        known_passengers = numbers

        # Adds to the list of Available Queues
        # TODO Automate this or allow user to customize
        add_to_av_queues(a_queue_list)

        # Represent the number of Drivers to create
        print(lines)
        print("*   Please enter the number of new Drivers you hired.")
        print("*   Our travel locations are: UWI, Papine, Liguanea & Half-Way-Tree.")
        # TODO Read from file all travel locations and display - replace the line above
        no_of_drivers = int(input())
        driver_lst =[]
        # Creates the Drivers with input information
        for i in range(no_of_drivers):
            print(
                "*   Enter the Drivers information.\n*   In the format - \"FirstName, LastName, CarMake|Model, LocationDestination\"")

            driver_info = input().strip().split(",")
            # Driver ADT is created
            driver = make_new_driver(
                driver_info[0], driver_info[1], driver_info[2])
            driver_lst.append(driver)
            # Driver gets added to a location
            a_queue_enqueue(get_a_queue(driver_info[3], a_queue_list), driver)
            print("\n" + lines)
        print("What would you like to do?")
        print("1:   Manage Drivers\n 2:  Manage Locations\n3:    Manage Rates\n 4:  Manage Customers.")
        choice = int(input())

        no_of_known_passengers = int(input())

        for i in range(no_of_known_passengers):
            print("\n*   In the format \"#######,Failed-trips\"")
            print(f"*   Please enter the 7-digit phone number for Passenger {i + 1} and the number of Failed Attempts: ")
            passenger = list(map(int, input().strip().split(",")))
            key = passenger[0]
            value = passenger[1]
            known_passengers[key] = value

        # Cost price per travel
        fare = float(input("\n*   Please enter the price for a single travel: $"))

        print("\n" + lines + "\n" + lines)
        print("*   Setup now completed.")
        print("*   Moving on into the User side.")
        print(lines + "\n")
        youba()

#################################################################################
#################################################################################


