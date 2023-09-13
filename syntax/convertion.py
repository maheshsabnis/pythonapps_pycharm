price = input('Enter Price')
tax = input('Enter Tax')

print(type(price))

net_price = float(price) * float(tax) / 100

print(f'The net price is ${net_price}')
# Print the type of the data, this is str 
print(type(price))
# This will print type float
print(type(net_price))