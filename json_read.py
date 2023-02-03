"""
Shows how to read a JSON data file using the json module.
"""

import json


def main():
    """
    A simple method to read a JSON data file using the json module's loads() function
    """
    # open the file in read mode
    f = open("data/nonsense_literature.json", "r")

    all_text = f.read()  # get all text in file as a string
    list_of_works = json.loads(all_text)  # return a list of all works

    # loop through each literature work
    for work in list_of_works:
        msg = "{} {} - {}".format(work["First Name"], work["Last Name"], work["Title"])
        print(msg)


# ------------------------------------------------------------ #
# If this file is being run directly, call the main method ... #
if __name__ == "__main__":
    main()
