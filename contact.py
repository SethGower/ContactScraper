#!/usr/bin/python
import csv


def main():
    all_ehouse = load('./files/eHouse-contact.csv')
    on_floor = gen_with_years('On Floor', (19, 19), all_ehouse)
    alumni = gen_with_years('Alumni', (16, 18), all_ehouse)

    print('Writing CSV files')
    write(all_ehouse, './files/all_ehouse.csv')
    write(alumni, './files/alumni.csv')
    write(on_floor, './files/on_floor.csv')


def gen_with_years(list_name, year_range, total_list):
    output_list = []

    for person in total_list:
        if int(person['Years Lived on Engineering House'][-2:]) in range(year_range[0], year_range[1]+1):
            output_list.append(person)
            print('Adding', person['First Name'],
                  person['Last Name'], person['Years Lived on Engineering House'], 'to', list_name)
    return output_list


def load(filename):
    output_list = []
    with open(filename, 'r') as infile:
        reader = csv.DictReader(infile)
        for row in reader:
            if row['First Name'] != '':
                output_list.append(row)
    return output_list


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
