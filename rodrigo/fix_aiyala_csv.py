#!/usr/bin/env python
# -*- coding: utf-8 -*-

from csv import reader, writer

PATH_FILE_INPUT = "aiyala_levy_theaters_2017_07_10.csv"
PATH_FILE_OUTPUT = "aiyala_levy_theaters_2017_07_10_output.csv"


# 1) get the address column (that has the number as well) and split it in two columns
# the address (with the address without number) and the number (address number)

with open(PATH_FILE_INPUT, "r") as csv_input:
    # read the CSV
    read_CSV = reader(csv_input, delimiter=',')

    # get the header of the CSV
    header = next(read_CSV)
    # add a new column, with the number of the address
    header.append("number")
    # get the index of the column "address"
    index_address = header.index("address")

    new_CSV = []
    new_CSV.append(header)

    len_header = len(header)
    
    for row in read_CSV:

        # remove the bad columns without header
        while len(row) > len(header):
            row.pop()  # remove the last column

        # put the address in lower case and replace the strings
        line = row[index_address].lower()
        line = line.replace("r.", "rua", 1).replace("av.", "avenida", 1).replace("pç.", "praça", 1)

        try:
            # split the address with the number, using the first occurrence
            address, number = line.split(",", 1)
        except ValueError:
            # if it is not possible to unpack the line, it means that there is not number
            address, number = line, ""

        # remove the extra spaces of the variables
        address = address.strip()
        number = number.strip()

        # add the address and the number into the CSV
        row[index_address] = address
        row.append(number)

        new_CSV.append(row)
        #print(row, "\n")

    #for row in new_CSV:
     #   print(row, "\n")

    # 2) save the result in the output
    with open(PATH_FILE_OUTPUT, "w") as csv_output:
        writer = writer(csv_output, lineterminator='\n')
        writer.writerows(new_CSV)
    

