# The DictReader class allows you to create an object like
# a regular CSV reader. But it maps the information of each line
# to a dictionary (dict) whose keys are specified by
# the values of the first line.

import csv
sum_of_salary = 0
tax = 0
with open('./../files/data.csv') as f:
    csv_data = csv.DictReader(f, delimiter='\t')
    # skip the header
    next(csv_data)
    # Show the data
    print("id \t name\t address \t city\t income \t tax")
    for data in csv_data:
        print(f" {data['id']} {data['name']} {data['address']} {data['city']} \t \t {data['income']} {float(data['income']) * 0.2}")
        sum_of_salary+= float(data['income'])

    print(f"Sum of Salary = {sum_of_salary}")
