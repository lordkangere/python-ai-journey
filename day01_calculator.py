item_name = input('item: ')
unit_price = float(input('whats the price?'))
quantity = int(input('Quantity: '))
results = unit_price * quantity
print()
print("------RESULTS-----")
print(f"{unit_price:,.2F} * {quantity} = {results:,.2f}")