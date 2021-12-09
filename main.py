# coding=utf-8

import csv
import random


# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print("Hi, {0}".format(name))  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

    # read in names and numbers from .csv
    with open('data-secret-santa.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0

        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1

            else:
                print(f'\t name: {row[0]} phoneNumber: {row[1]}')
                line_count += 1

        print(f'Read {line_count} lines.')

    with open("data-secret-santa.csv", 'r') as data:

        # TODO: fix to NOT read first row (name and number attribute name)

        line_count = 0

        reader = csv.reader(data)
        # if line_count != 0:

        csv_Dict = {rows[0]: rows[1] for rows in reader}

        line_count += 1

    for key in csv_Dict:
        var = key, csv_Dict[key]
        print(var)

    # print(csv_Dict)
    # var = csv_Dict["Justin Hayes"]
    # print(var)

    # NOW WE HAVE a dictionary with name, number pairs
    # NAME , PhoneNumber

    pair_Dict = {}

    # could randomize names into a new structure then destroy each once selected

    # keys = csv_Dict.keys()
    keys = list(csv_Dict.keys())

    for key in csv_Dict:

        # we now have all the KEYS Here

        # this while loop ensures cannot be assigned self as receiver
        while True:
            rand_key = random.choice(keys)

            if rand_key != key:
                # Now here remove rand_key from keys list
                keys.remove(rand_key)
                break

        pair_Dict[key] = rand_key

    print("\nThe final result map\n")

    for key in pair_Dict:
        var = key, pair_Dict[key]
        print(var)

    # for name in csv_Dict
    # assign random and non-repeatable partner from names in csv_Dict
    # Maybe utilize set?

    # Now we need to assign pairs, (new map?)
    # for each name in csv_Dict, give them pair
    # This reciever cannot be selected again

    # notify through text

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
