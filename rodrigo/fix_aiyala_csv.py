#!/usr/bin/env python
# -*- coding: utf-8 -*-

# roll back pip: python3 -m pip install --user --upgrade pip==9.0.3

import pandas as pd 

PATH_FILE_INPUT = "aiyala_levy_theaters_2017_07_10.csv"
PATH_FILE_OUTPUT = "aiyala_levy_theaters_2017_07_10_output.csv"

df = pd.read_csv(PATH_FILE_INPUT)

# creating a blank series 
address_series = pd.Series([])
number_series = pd.Series([])

#  df.loc[i, 'number'] = number

for i in range(0, len(df)):
    address_with_number = df["address"][i]

    line = str(address_with_number).lower()
    line = line.replace("r.", "rua", 1).replace("av.", "avenida", 1).replace("pç.", "praça", 1)

    # avoid problem with nan values, change to white space
    if line == "nan":
        address, number = "", ""
    else:
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
    address_series[i] = address
    number_series[i] = number

# remove the old address column ...
del df["address"]
# ... and create the new ones
df["address"] = address_series
df["number"] = number_series

# fill the NaN values with white space
df = df.fillna("")

# convert dataframe to CSV
df.to_csv(PATH_FILE_OUTPUT, encoding='utf-8')


#print(df.head(15))

print(df[['address', 'number']].head(15))

"""
print("\n")

print(df[['address', 'number']])
"""
    
    













'''
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

    for row in read_CSV:
        new_CSV.append(row)
    
    for row in new_CSV:

        print("len(row): ", len(row), " - len(header): ", len(header))
        # remove the bad columns without header
        while len(row) > len(header):
            print(row)
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
        
        print(row, "\n")

    #for row in new_CSV:
     #   print(row, "\n")

    # 2) save the result in the output
    with open(PATH_FILE_OUTPUT, "w") as csv_output:
        writer = writer(csv_output, lineterminator='\n')
        writer.writerows(new_CSV)
'''    

