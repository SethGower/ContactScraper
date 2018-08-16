#!/usr/bin/python
import csv


def main():
    all_ehouse = []
    on_floor = []
    alumni = []

    alumni_years = [('16', '17'), ('16', '18'), ('17', '18'),
                    ('15', '16'), ('15', '17'), ('14', '15'), ('14', '16')]

    load(all_ehouse, './eHouse-contact.csv')
    print('Creating on_floor list')
    for person in all_ehouse:
        if '19' in person['Years Lived on Engineering House'] and person['First Name'] != '':
            print('Adding', person['First Name'],
                  person['Last Name'], 'to on_floor')
            on_floor.append(person)

    print()
    print('Creating Alumni List')
    for person in all_ehouse:
        for tup in alumni_years:
            if (tup[0] in person['Years Lived on Engineering House'] or tup[1] in person['Years Lived on Engineering House']) and person not in alumni and person not in on_floor:
                print('Adding', person['First Name'],
                      person['Last Name'], 'to alumni')
                alumni.append(person)

    print('Writing CSV files')
    write(all_ehouse, 'all_ehouse.csv')
    write(alumni, 'alumni.csv')
    write(on_floor, 'on_floor.csv')


def load(outputList, filename):
    with open(filename, 'r') as infile:
        reader = csv.DictReader(infile)
        for row in reader:
            if row['First Name'] != '':
                outputList.append(row)


def write(inputDicts, filename):
    with open(filename, 'w') as outfile:
        fieldnames = ['Last Name', 'First Name',
                      'Display Name', 'Primary Email', 'Mobile Phone', 'Years Lived on Engineering House']
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)

        writer.writeheader()
        for row in inputDicts:
            if row['Email Address'] != '':
                writer.writerow({'Last Name': row['Last Name'], 'First Name': row['First Name'], 'Display Name': row['First Name'] + ' ' + row['Last Name'],
                                 'Primary Email': row['Email Address'], 'Mobile Phone': row['Phone Number'], 'Years Lived on Engineering House': row['Years Lived on Engineering House']})


if __name__ == '__main__':
    main()
