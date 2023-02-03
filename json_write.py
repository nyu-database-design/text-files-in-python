"""
Shows how to write to a JSON data file using the json module's dumps() function.
"""

import json


def main():
    """
    A simple method to write to a JSON data file using the json module's dumps() function
    """

    # a list of dictionaries, containing our data
    works = [
        {
            "Last Name": "Carroll",
            "First Name": "Lewis",
            "Title": "Jabberwocky",
            "Year": 1871,
        },
        {
            "Last Name": "Lear",
            "First Name": "Edward",
            "Title": "The Jumblies",
            "Year": 1910,
        },
        {
            "Last Name": "Bishop",
            "First Name": "Elizabeth",
            "Title": "The Man-Moth",
            "Year": 1946,
        },
    ]

    # create proper JSON data from this list of dictionaries, indent it nicely
    json_data = json.dumps(works, indent=2)

    # write that JSON data to the file
    f = open("data/nonsense_literature.json", "w")
    f.write(json_data)

    # when done, always close the file
    f.close()


# ------------------------------------------------------------ #
# If this file is being run directly, call the main method ... #
if __name__ == "__main__":
    main()
