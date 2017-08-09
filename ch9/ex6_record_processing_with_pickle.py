#!/usr/bin/python3
import pickle

# This program builds on the example from CH6, but instead of reading/writing
# from text files, we'll read/write to a file of pickled objects.

def main():
    # Ask the user where the file is
    roster_filename = input('What is the name of the roster file? ')

    # Ask the user to enter data or display data
    choice = input('Enter 1 for Roster Entry, 2 for Roster Display: ')
    if choice == '1':
        build_roster(roster_filename)
    elif choice == '2':
        display_roster(roster_filename)


def build_roster(roster_filename):
    # This function will repeatedly ask the user for data to build player
    # dict objects and then write them to our file object with roster_filename.
    # Note that we are opening the file for writing in binary mode this time
    # denoted by the 'wb'.
    roster_file = open(roster_filename, 'wb')
    while True:
        player = {}
        # Ask for some data from the user
        player['name'] = input('Enter Player Name: ')
        player['team'] = input('Enter Player Team: ')
        player['position'] = input('Enter Position: ')
        player['salary'] = input('Enter Salary: ')

        # Write the player object to the file using pickle.dump
        pickle.dump(player, roster_file)

        print('----- {} written to "{}"'.format(player['name'],
                                                roster_filename))

        # Ask the user if they want to continue, otherwise break the loop
        more_players = input('Do you want to continue (Y/N)? ')
        if more_players != 'Y':
            break

    roster_file.close()
    print('Finished writing to file')


def display_roster(roster_filename):
    # This function will read objects from roster_filename. We will open the
    # file in binary read mode and use pickle to load our objects. We'll
    # wait until the EOFError is thrown to break our loop.
    roster_file = open(roster_filename, 'rb')

    # We'll use while True and use an explicit break when the EOFError occurs
    while True:
      try:
        player = pickle.load(roster_file)
        # Now we have the four pieces of our player record. We can print it out.
        print('{} plays {} for the {} and costs ${}'.format(
            player['name'], player['position'], player['team'], player['salary']
        ))
      except EOFError:
        break

    roster_file.close()
    print('Finished reading from file')


main()
