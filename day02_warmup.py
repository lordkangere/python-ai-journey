age = int(input("Type in your age: "))
ticket_price = 999

#Under 5 is free, under 18 is half price (150), anyone else pays full
#  price (300).
if age < 0:
        print("invalid input")
else:
        if age < 5:
                ticket_price = 0
        elif age <18:
                ticket_price = 150
        else:
                ticket_price = 300
        print(f"Your ticket price is: {ticket_price:,.2f} ")



