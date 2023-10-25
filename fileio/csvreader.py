import csv
# OPen the CSV file
f = open('./../files/data.csv')
# pass the object f to reader() method of the CSV
csv_data = csv.reader(f)

# print the data
for line in csv_data:
    print(line)
# close the file
f.close()
