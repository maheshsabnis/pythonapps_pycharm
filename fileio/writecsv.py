import csv

# defne a dictionary

employees = [
    {'id': 1001, 'name': 'Mahesh', 'salary': 500000},
    {'id': 1002, 'name': 'Tejas', 'salary': 600000},
    {'id': 1003, 'name': 'Vikram', 'salary': 700000},
    {'id': 1004, 'name': 'Suprotim', 'salary': 800000},
    {'id': 1005, 'name': 'Manish', 'salary': 900000},
    {'id': 1006, 'name': 'Sachin', 'salary': 100000},
    {'id': 1007, 'name': 'Saket', 'salary': 200000},
    {'id': 1008, 'name': 'Abhijeet', 'salary': 300000},
    {'id': 1009, 'name': 'Kiran', 'salary': 400000},
    {'id': 1010, 'name': 'Ravi', 'salary': 800000},
]
# read the keys
dict = employees[0]
keys = dict.keys()

with open('./../files/employees_data.csv', 'w') as f:
    writer = csv.writer(f)
    # Write keys
    writer.writerow(keys)
    for emp in employees:
        writer.writerow(emp.values())
    f.close()
