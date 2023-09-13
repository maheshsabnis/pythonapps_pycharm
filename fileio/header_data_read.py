import csv

with open('./../files/data.csv') as f:
    csv_data = csv.reader(f)
    for record_no, record in enumerate(csv_data,1):
        if record_no == 1:
            print('Header')
            print(record)
            print('')
        else:
            print(record)
    f.close()
