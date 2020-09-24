#################################################################################
# CJ test to see if I am on the correct branch.
"""
Youba Ltd. is a startup company that aims to revolutionize the local public transportation by
introducing a brand new way for travellers to connect with drivers. Users only need
to have a cellphone to utilize the service. Given your knowledge of ADTs, Youba Ltd.
has contracted you to implement the platform for thier service.
"""

import os

#Dwight's Test Comment

#################################################################################
# Driver Section
#################################################################################


def make_new_driver(first_name, last_name, car_make_and_model):
    """
    Constructs an ADT for a new Driver

    Args:
        first_name: Drivers first name
        last_name: Drivers last name
        car_make_and_model: Drivers car make and model

    Returns:
        driver: A Driver ADT
    """
    trips_completed = 0
    return ("Driver", [first_name, last_name, car_make_and_model,
                       trips_completed])


def make_driver(first_name, last_name, car_make_and_model, trips_completed):
    """
    Constructs an ADT for an existing Driver

    Args:
        first_name: Drivers first name
        last_name: Drivers last name
        car_make_and_model: Drivers car make and model
        trips_completed: Number of trips made per day

    Returns:
        driver: A Driver ADT
    """
    return ("Driver", [first_name, last_name, car_make_and_model,
                       trips_completed])


def is_driver(driver):
    """
    Determines whether an object is a Driver

    Args:
        driver: A Driver ADT

    Returns:
        boolean: True or False
    """
    if len(driver) == 2 and driver[0] == "Driver":
        driver_info = get_driver_info(driver)
        if type(driver_info) == type([]) and len(driver_info) == 4:
            return True
    return False


def get_driver_info(driver):
    """
    Gets the list of Driver details

    Args:
        driver: A Driver ADT

    Returns:
        driver_info: list of Driver information
    """
    driver_info = driver[1]
    return driver_info


# Gets the Drivers first name


def get_first_name(driver):
    """


    Args:
        driver: A Driver ADT

    Returns:
        f_name: Drivers first name
    """
    f_name = get_driver_info(driver)[0]
    return f_name


def get_last_name(driver):
    """
    Gets the Drivers last name

    Args:
        driver: A Driver ADT

    Returns:
        l_name: Drivers last name
    """
    l_name = get_driver_info(driver)[1]
    return l_name


def get_make_and_model(driver):
    """
    Gets the Drivers car make and model

    Args:
        driver: A Driver ADT

    Returns:
        make_model: Drivers care make and model
    """
    make_model = get_driver_info(driver)[2]
    return make_model


def change_make_and_model(driver, new_make_model):
    """
    Updates the Drivers car make and model

    Args:
        driver: A Driver ADT

    Returns:
        None
    """
    if is_driver(driver):
        driver_info = get_driver_info(driver)
        driver_info[2] = new_make_model
    else:
        print("*\n*   ERROR: ")
        print("*   Didn't receive a Driver\n")


def get_trips_completed(driver):
    """
    Gets the Drivers number of trips completed for the day

    Args:
        driver: A Driver ADT

    Returns:
        trips: Drivers total trips completed
    """
    trips = get_driver_info(driver)[3]
    return trips


def increase_trips_completed(driver):
    """
    Increases the number of trips a Driver makes

    Args:
        driver: A Driver ADT

    Returns:
        None
    """
    driver_info = get_driver_info(driver)
    driver_info[3] = get_trips_completed(driver) + 1


def is_driver_new(driver):
    """
    Determines whether a Driver is new or not

    Args:
        driver: A Driver ADT

    Returns:
        boolean: True or False
    """
    num = get_trips_completed(driver)
    if num == 0:
        return True
    return False


#################################################################################
# Availability Queue Section
#################################################################################


def make_availability_queue(location):
    """
    Creates an Availability Queue

    Args:
        location: A location

    Returns:
        a_queue: An Availability Queue ADT
    """
    a_queue = ("AvailabilityQueue", location, [])
    return a_queue


def get_queue_contents(a_queue):
    """
    Gets Availability Queue contents

    Args:
        a_queue: An Availability Queue ADT

    Returns:
        queue_contents: The list of Drivers at an Availability Queue
    """
    queue_contents = a_queue[2]
    return queue_contents


def get_a_queue(location_name, a_queue_list):
    """
    Gets the Availability Queue from the list based on location

    Args:
        location_name: A location
        a_queue_list: A list of Availability Queues

    Returns:
        a_queue: An Availability Queue ADT
    """
    for a_queue in a_queue_list:
        if get_location(a_queue) == location_name:
            return a_queue
    print("There are no Availability Queues for this location.")
    return make_availability_queue("")


def is_a_queue(a_queue):
    """
    Check if an Availability Queue is empty/ doesn't exist.
    This is separate from an availability queue not having drivers.

    Args:
        a_queue: An Availability Queue ADT

    Returns:
        boolean: True or False
    """
    if get_location(a_queue) == "":
        return False
    return True


def get_location(a_queue):
    """
    Gets the Availability Queue location name

    Args:
        a_queue: An Availability Queue ADT

    Returns:
        location: The location of an Availability Queue
    """
    location = get_driver_info(a_queue)
    return location


def a_queue_front(a_queue):
    """
    Returns the first Driver in the Availability Queue list

    Args:
        a_queue: An Availability Queue ADT

    Returns:
        driver: An ADT representing a Driver
    """
    if is_a_queue_empty(a_queue):
        print("\nThere are no Taxi Drivers present at the moment.\n")
        return make_availability_queue("")
    else:
        return get_queue_contents(a_queue)[0]


def a_queue_enqueue(a_queue, driver):
    """
    Adds a driver to an Availability Queue list

    Args:
        a_queue: An Availability Queue ADT
        driver: A Driver ADT

    Returns:
        None
    """
    get_queue_contents(a_queue).append(driver)


def a_queue_dequeue(a_queue):
    """
    Removes a driver from an Availability Queue list

    Args:
        a_queue: An Availability Queue ADT

    Returns:
        None
    """
    if is_a_queue_empty(a_queue):
        print("\nERROR.\nThere are no Drivers at this Location to remove.\n")
    else:
        get_queue_contents(a_queue).pop(0)


def is_a_queue_empty(a_queue):
    """
    Checks to see if an Availability Queue is Empty

    Args:
        a_queue: An Availability Queue ADT

    Returns:
        boolean: True or False
    """
    if get_queue_contents(a_queue) == []:
        return True
    return False


def add_a_queue(a_queue, a_queue_list):
    """
    Adds an Availability Queue to the list of Availability Queues

    Args:
        a_queue: An Availability Queue ADT
        a_queue_list: A list of Availability Queues

    Returns:
        None
    """
    a_queue_list.append(a_queue)


def remove_a_queue(a_queue, a_queue_list):
    """
    Removes an Availability Queue from the list of Availability Queues

    Args:
        a_queue: An Availability Queue ADT
        a_queue_list: A list of Availability Queues

    Returns:
        None
    """
    x = -1
    for i in range(len(a_queue_list)):
        if a_queue_list[i] == a_queue:
            x = i
            break

    if x != -1:
        a_queue_list.pop(x)
    else:
        print("There are no Availability Queues for this location.\n")


#################################################################################
# Fair Calculation Section
#################################################################################

# Calculates the discount for a customer


def calculate_discount(phone_num, passengers):
    """
    Calculates the discount to be applied for a customer

    Args:
        phone_num: Customers telephone number
        passengers: Dictionary of Customers information

    Returns:
        failed_attempts: A float value of discounted price
    """

    for number, failed_attempts in passengers.items():
        if number == phone_num:
            return failed_attempts * 0.10

    passengers[phone_num] = 0
    return 0.00


# Calculates the final fare for the customer


def calculate_fare(phone_num, price, passengers):
    """
    Calculates the customers total fare after discount has been applied

    Args:
        phone_num: Customers telephone number
        price: The cost per taxi trip
        passengers: Dictionary of Customers information

    Returns:
        discounted_fare: Discounted price
    """

    discount = calculate_discount(phone_num, passengers)

    discounted_fare = price - (price * discount)

    if discounted_fare < 0.00:
        return 0.00
    return discounted_fare


#################################################################################
# Taxi Section
#################################################################################

# Moves a Driver from one location to the other


def move_taxi(start_location, end_location, a_queue_list):
    """
    Moves a taxi from one location to another with an Availability Queue list

    Args:
        start_location: Customers current location
        end_location: Customers desired destination
        a_queue_list: A list of Availability Queues

    Returns:
        None
    """
    if is_a_queue_empty(get_a_queue(start_location, a_queue_list)):
        print("*   No driver at location.\n")
    else:
        driver = a_queue_front(get_a_queue(start_location, a_queue_list))
        a_queue_dequeue(get_a_queue(start_location, a_queue_list))
        a_queue_enqueue(get_a_queue(end_location, a_queue_list), driver)
        increase_trips_completed(driver)


def request_taxi(passenger_phone_num, passenger_location, passenger_destination, price, passengers, a_queue_list):
    """
    Requests a taxi for a customer at a specific location

    Args:
        passenger_phone_num: Customers telephone number
        passenger_location: Customers current location
        passenger_destination: Customers desired destination
        price: Cost per trip
        passengers: A dictionary of customers and their failed attempts
        a_queue_list: A list of Availability Queues

    Returns:
       None
    """
    if passenger_location == passenger_destination:
        print("\n*\n*   Start and end locations are the same!\n*\n")
    else:
        # Fare for the trip is calculated
        trip_fare = calculate_fare(passenger_phone_num, price, passengers)
        print("*   Your final fare is ${}.".format(trip_fare))

        option = input(
            "*   Enter \"Y\" to confirm the trip or \"N\" to cancel - ")
        if option == "Y" or option == "y":
            if is_a_queue_empty(get_a_queue(passenger_location, a_queue_list)):
                passengers[passenger_phone_num] += 1
                print("\n*   Unfortunately, there are no drivers at that location.")
                print("*   We apologize for any inconvenience.")
                print("*   You will receive a 10% discount on your next trip.")
            else:
                print(lines)
                print("*   A Taxi is on the way.\n")
                print(lines)
                move_taxi(passenger_location,
                          passenger_destination, a_queue_list)
        else:
            print(lines)
            print("*   Cancelling trip")
            print(lines)


#################################################################################
# Youba Section
#################################################################################

def youba():
    """
    Handles the Customer side of the service

    Args:
        None

    Returns:
        None
    """
    print(lines)
    print("*   Currently, there are only 4 Destinations that we cover.\n*   There will be more in the Future.")
    print("*   They are: UWI, Papine, Liguanea & Half-Way-Tree.")
    print("*   The price per trip is ${}\n*   Discounts will be added where neccessary.".format(fare))
    print(lines)
    print("*   Would you like to Request our services?")
    print("*   Enter Y for Yes")
    print("*   Enter N for No\n")
    request = input()

    while (request == "Y" or request == "y"):
        print(lines)
        print("*   What is your phone number?:")
        passenger_phone_num = int(input())
        print("*   What is your Location?:")
        passenger_location = input()
        print("*   What is your Destination?:")
        passenger_destination = input()

        request_taxi(passenger_phone_num, passenger_location,
                     passenger_destination, fare, known_passengers, a_queue_list)

        print("\n*   Would you like to Request our services again?")
        print("*   Enter Y for Yes")
        print("*   Enter N for No")
        request = input()

    print(lines)
    print("Thank you for trying Youba. Please come again.\n")
    print("A list will be printed upon exit.")
    print("List of Drivers and Number of Jobs Completed.")

    for a_queue in a_queue_list:
        for driver in get_queue_contents(a_queue):
            print(get_first_name(driver) + "\t" + get_last_name(driver) + "\t" +
                  str(get_trips_completed(driver)))
    print(lines)
    print("*   List of Locations and Drivers for those that worked today.")
    print("* Current Location\tDriver Name\tCar Make & Model")

    for a_queue in a_queue_list:
        if not is_a_queue_empty(a_queue):
            driver = a_queue_front(a_queue)
            print("* " + get_location(a_queue) + "\t\t" + get_first_name(driver) + " " +
                  get_last_name(driver) + "\t\t" + get_make_and_model(driver))


#################################################################################
# Main Section
#################################################################################


if __name__ == '__main__':
    lines = "********************************************************************"
    print(lines)
    print("*   Welcome to the Admin side.")
    print("*   Please setup the Youba data with the neccesary information.")
    print(lines + "\n")

    # Makes new Availability Queues
    a_queue_UWI = make_availability_queue("UWI")
    a_queue_Papine = make_availability_queue("Papine")
    a_queue_Liguanea = make_availability_queue("Liguanea")
    a_queue_HalfWayTree = make_availability_queue("Half-Way-Tree")

    # A list of queues
    a_queue_list = list()  # TODO Generate a list of Availability Queues
    # A dictionary of customers and their failed attempts
    known_passengers = dict()  # Generate a dictionary of customer info

    # Adds to the list of Available Queues
    # TODO Automate this or allow user to customize
    add_a_queue(a_queue_UWI, a_queue_list)
    add_a_queue(a_queue_Papine, a_queue_list)
    add_a_queue(a_queue_Liguanea, a_queue_list)
    add_a_queue(a_queue_HalfWayTree, a_queue_list)

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
        print("*   Please enter the 7-digit phone number for Passenger {} and the number of Failed Attempts: ".format(
            i + 1))
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
