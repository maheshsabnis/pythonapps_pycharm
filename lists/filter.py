names = ['Jay','Mahesh', 'Mukesh Sabnis', 'Amit', 'Abhijit','Mayuresh', 'Suprotim', 'Vikram', 'Narayan Dev']

# Filter those strings having length more that 7

morethan7 = filter(lambda record:len(record)>7, names)

for record in morethan7:
    print(record)

print()
# Starts with 'A'

startswithA = filter(lambda record:record.startswith('A'),names)
for record in startswithA:
    print(record)

    