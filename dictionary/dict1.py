# Define Dictionary

employee = {
    'EmpNo':101,
    'EmpName':'Mahesh',
    'DeptName': 'IT'
} 

print(employee.get('EmpNo'))

print(employee.keys())
print(employee.values())

for v in employee.items():
    print(v)
    
# defining a funciton that will be creating a list of dictionary
employees = [];
def listGenerator(record):
    employees.append(record)    

for i in range(10):
    empno = input('Enter EmpNo')
    empname = input('Enter EmpName')
    deptname = input('Enter DeptName')
    
    emp = {
        'EmpNo':int(empno),
        'EmpName':empname,
        'DeptName':deptname
    }
    listGenerator(emp)


print('List of Employees')

for emp in employees:
    print(f"{emp['EmpNo']} {emp['EmpName']} {emp['DeptName']}")
        