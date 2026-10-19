item_name = input('item: ')
unit_price = float(input('whats the price?'))
quantity = int(input('Quantity: '))
results = unit_price * quantity
print()
print("------RESULTS-----")
print(f"{unit_price:,.2F} * {quantity} = {results:,.2f}")

quantity = 60
if quantity >= 100:
    discount = 0.10
elif quantity >= 50:
    discount = 0.50
else :
    discount = 0

print(f"Discount : {discount}")

age = 38
has_id = True

if age >= 18 and has_id:
    print("Allowed In")
if age <18 and not has_id:
    print("Not Allowed")

price = float(input('Unit price: '))
if price < 0:
    print("price must be above zero")
else:
    print("price accepted")

materials = ['cement','ballast','sand']
print(materials[0])
print(materials[2])
materials.append('steel')
print(materials)

for material in materials:
    print(material)

count = 0
while count <= 8:
    print(f"Round: {count}") 
    count +=1

while True:
    answer = input('Type stop to End.')    
    if answer == 'stop':
        break
    print('You typed', answer)

total = 0
prices = [100,250,65]

for price in prices:
    total += price

    print(total)

names = ['cement','sand']
costs = ['10300','4600']

for i in range (len(names)):
    print(i +1,names[i],costs[i])
