import csv

# defne a dictionary

employees1 = [
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
dict = employees1[0]
keys = dict.keys()

with open('./../files/employees_data_new.csv', 'w', newline='') as f:
    writable = csv.DictWriter(f, fieldnames=keys)
    # Write keys
    writable.writeheader()
    writable.writerows(employees1)
