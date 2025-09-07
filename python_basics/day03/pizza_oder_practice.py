print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese on your pizza? Y or N: ")
    
basic_price = 0
if size == "S":
    basic_price += 15
elif size == "M":
    basic_price += 20
elif size == "L":
    basic_price += 25
else:
    print("You entered wrong size")


if pepperoni == "Y":
    if size == "S":
        basic_price += 2
    else:
        basic_price += 3
        
if extra_cheese == "Y":
    basic_price += 1
    
print("Final price is : $", basic_price)

