name ='kangere nganga'
print(f"Hello,{name}" )

var_1 = 23
var_2 = 45
print(var_1 + var_2)
print(var_1 - var_2)
print(var_1 * var_2)

user_name = input('Hey buddy, whats your name?')
print(f"Good Morning {user_name}, how are you?")

a = float(input('Enter the first no. '))
b = float(input('Enter the second no. '))

larger_number = max(a,b)
results = larger_number*2
print(f"The larger no. doubled is , {results:,.2f}")

print(type(75))
print(type(78.94))
print(type("jonathan"))
print(type(True))


item_name = input("What do you want:? ")
unit_price = float(input('whats the unit price:? '))
quantity = int(input('Quantity: '))
total = unit_price * quantity
print()
print('------RESULTS------')
print(f"{quantity} * {unit_price:,.4f} = {total:,.2f}")
print(item_name.upper())

print("5"+"4")