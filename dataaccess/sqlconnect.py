# import pyodbc
import pyodbc
# Connect to DB
connStr = "Driver={ODBC Driver 17 for SQL Server};SERVER=127.0.0.1;DATABASE=UCompany;UID=sa;PWD=MyPass@word;Trust_Connection=yes;"
conn = pyodbc.connect(connStr)

# Define a Cursor

cursor = conn.cursor()

# Execute the Select Statement
cursor.execute("Select * from Department")

for dept in cursor:
    print(dept)

# insert Record

dno = int(input('Enter DeptNo'))
dname = input('Enter Dept Name')
location = input('Enter Location')
capacity = int(input('Enter Capacity'))

insertStatement = f'''
    INSERT into Department(DeptNo,DeptName,Location,Capacity) Values ({dno},'{dname}', '{location}',{capacity})
'''

cursor.execute(insertStatement)
cursor.commit()

# Execute the Select Statement
cursor.execute("Select * from Department")

for dept in cursor:
    print(dept)

# Perform Update
print('Performing the Update')

dno = int(input('Enter DeptNo'))
dname = input('Enter Dept Name')
location = input('Enter Location')
capacity = int(input('Enter Capacity'))

strUpdate = f'''
   Update Department Set DeptName='{dname}', Location='{location}', Capacity={capacity}
   where DeptNo={dno}
'''

cursor.execute(strUpdate)
cursor.execute(f"Select * from Department where DeptNo={dno}")
for dept in cursor:
    print(dept)

# For Delete

dno = int(input('Enter DeptNo for Delete'))

cursor.execute(f"Delete From Department where DeptNo={dno}")
cursor.execute("Select * from Department")
for dept in cursor:
    print(dept)






