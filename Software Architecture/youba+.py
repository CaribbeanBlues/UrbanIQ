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

dest_db = 'database/destinations_database.csv'
num_db = 'database/numbers_database.csv'
queue_dict = {}
with open(dest_db) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    destinations = []
    for row in reader:
        destinations.append(row[1])
with open(num_db) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    numbers = {}
    for row in reader:
        numbers[row[0]] = row[1]


def make_av_queues():
    for destination in destinations:
        queue_dict[destination] = queue.make_availability_queue(destination)
    return queue_dict


def add_to_av_queues(a_queue_list):
    return make_av_queues()

def add_destination(loc):
    with open(destination, 'a') as f:
        f.write(loc)

# TODO Make each section its own .py file
# TODO Run Pycharm's code analyzer

#################################################################################
# Main Section
#################################################################################


if __name__ == '__main__':
    lines = "********************************************************************"
    print(lines)
    print("*   Welcome to the Admin side.")
    print("*   Please setup the Youba data with the necessary information.")
    print(lines + "\n")

    # Makes new Availability Queues

    # A list of queues
    a_queue_list = make_av_queues()  # TODO Generate a list of Availability Queues
    # A dictionary of customers and their failed attempts
    known_passengers = numbers

    # Adds to the list of Available Queues
    # TODO Automate this or allow user to customiz
    add_to_av_queues(a_queue_list)

    # Represent the number of Drivers to create
    print(lines)
    print("*   Please enter the number of new Drivers you hired.")
    print("*   Our travel locations are: UWI, Papine, Liguanea & Half-Way-Tree.")
    # TODO Read from file all travel locations and display - replace the line above
    no_of_drivers = int(input())

    # Creates the Drivers with input information
    for i in range(no_of_drivers):
        print(
            "*   Enter the Drivers information.\n*   In the format - \"FirstName, LastName, CarMake|Model, LocationDestination\"")

        driver_info = input().strip().split(",")
        # Driver ADT is created
        driver = make_new_driver(
            driver_info[0], driver_info[1], driver_info[2])
        # Driver gets added to a location
        a_queue_enqueue(get_a_queue(driver_info[3], a_queue_list), driver)

    print("\n" + lines)
    print("*   Enter the number of Previous Passengers that did use our Service.")
    print("*   Passengers that have used our services before.")
    print("*   Known passengers get a 10% discount per trip they have failed to take before.")

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


# Good day! Welcome to Admin side! What would you like to do!
# 1. Manage Drivers: (should show a list of drivers)
#   1: Add New Driver
#   2: Edit Drivers
#   3: Delete Driver
# 2. Manage Destinations: (should show list of destinations)
#   1: Add new Destinations
#   2: Edit destinations
#   3: Delete Destinations
# 3. Manage Rates
#
#
# 4. Manage Customers (should show list of numbers and failed attempts)
#   1: Add new customer
#   2: Edit customer
#   3: Delete customer
