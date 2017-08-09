#!/usr/bin/python3

# This program will allow us to build and display a roster for a one-day
# fantasy sports league. It's a hot business to get into so let's finish our
# project before the laws ban these types of sites.

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
    # This function will repeatedly ask the user for data to build roster
    # entries and then write them to our file object with roster_filename.
    roster_file = open(roster_filename, 'w')
    while True:
        # Ask for some data from the user
        name = input('Enter Player Name: ')
        team = input('Enter Player Team: ')
        position = input('Enter Position: ')
        salary = input('Enter Salary: ')

        # Write this data on 4 lines to roster_file
        roster_file.write(name + '\n')
        roster_file.write(team + '\n')
        roster_file.write(position + '\n')
        roster_file.write(salary + '\n')

        print('----- {} written to "{}"'.format(name, roster_filename))

        # Ask the user if they want to continue, otherwise break the loop
        more_players = input('Do you want to continue (Y/N)? ')
        if more_players != 'Y':
            break

    roster_file.close()
    print('Finished writing to file')


def display_roster(roster_filename):
    # This function will read records from roster_filename. A record is
    # comprised of 4 lines from the file so we'll collect strings in batches of
    # 4 before outputting data to the user.
    roster_file = open(roster_filename)

    # This is our priming read to set the variable we'll use when looping.
    # Remember, readline will always return a string, and we want to strip the
    # newline character from the right side if it exists. If name is the empty
    # string, the loop will never execute
    name = roster_file.readline().rstrip()
    while name:
        # The next three lines are team, position, and salary respectively
        team = roster_file.readline().rstrip()
        position = roster_file.readline().rstrip()
        salary = roster_file.readline().rstrip()

        # Now we have the four pieces of our player record. We can print it out.
        print('{} plays {} for the {} and costs ${:,.2f}'.format(
            name, position, team, float(salary)
        ))

        # Now, we read into name again to prepare for the next iteration
        name = roster_file.readline().rstrip()

    roster_file.close()
    print('Finished reading from file')


main()
