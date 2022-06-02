"""
Created on June 1st, 2022 - Wednesday

The main function block for the best practices script practice.

@author jdglassman
"""

from time import sleep
import os

print("This is my file to demonstrate best practices.")

def process_data(data):
    """
    Processes data provided to the function.
    :param data: Input dataset.
    :return: Modified input dataset.
    """
    print("Beginning data processing...")
    modified_data = data + " that has been modified"
    sleep(3)
    print("Data processing finished.")
    return modified_data

def read_data_from_web():
    """
    Reads in data from the web.
    :return: Data obtained from the web.
    """
    print("Reading data from the Web...")
    data = "Data from the web"
    return data

def write_data_to_database(data):
    """
    Writes data from the web into a database.
    :param data: Data pulled from the web from read_data_from_web()
    :return: Nothing
    """
    print("Writing data to a database")
    print(data)

def main():
    """
    Executes all functions in the correct order
    :return: Nothing
    """
    data = read_data_from_web()
    modified_data = process_data(data)
    write_data_to_database(modified_data)

if __name__ == "__main__":
    main()