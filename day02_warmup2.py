#ask for a whole number and say which it is.
get_number = int(input("Type in any number: "))


if get_number % 2 == 0:
        Status = "Even Number"
else:
        Status = "Odd Number"
print(f"Your no. is {get_number} and it is an {Status}")
