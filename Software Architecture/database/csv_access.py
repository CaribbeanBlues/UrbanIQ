import csv
from csv import writer

dest_db = 'destinations_database.csv'
num_db = 'numbers_database.csv'


def get_all_destinations():
    """
    Loads all destinations from destinations_database.csv
    Returns: list of destinations from the CSV file

    """
    with open(dest_db) as f:
        reader = csv.reader(f)
        header_row = next(reader)
        destinations = []
        for row in reader:
            # destinations[int(row[0])] = row[1]
            destinations.append(row)
        return destinations


def insert_destination(destination):
    """
    Inserts a destination into destinations_database.csv
    Args: A dictionary containing the location and its ID

    """
    with open(dest_db, 'a+', newline='') as write_obj:
        csv_writer = writer(write_obj)
        csv_writer.writerow(destination)



def get_destinations(id):
    """

    Args:
        id: The ID of the destination

    Returns: Destination string of a given ID

    """
    destinations = get_all_destinations()
    try:
        return destinations[id]
    except KeyError:
        pass
    return {}

def delete_destination(dest_id):
    """
    Deletes a destination from the database
    Args:
        dest_id: id of destination

    Returns:

    """
    dest_id =- 1
    destinations = get_all_destinations()
    destinations.pop(dest_id)
    with open(dest_db, 'w+', newline='') as write_obj:
        csv_write = writer(write_obj)
        csv_write.writerow(("id", "destination"))
        for dest_row in destinations:
            csv_write.writerow(dest_row)

def edit_destination(dest_id, destination):
    destinations = get_all_destinations()
    print(destinations)
    # destinations[dest_id] = destinations
    # print(destinations)



# def insert_driver(driver):
#     """
#     Inserts a driveer into drivers_database.csv
#     Args:
#         driver: a list containing the driver's necessary information
#
#     """
#     with open()


print(delete_destination(5))
