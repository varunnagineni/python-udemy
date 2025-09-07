print("Welcome to the rollercoaster!")
height = int(input("What is you height in cm? "))
ticket_price = 0

if height > 120:
    age = int(input("You are eligible for rollercoaster ride, what is your age? "))
    if age > 18:
        print("Your ticket price is $12.")
        ticket_price = 12
    elif age < 12:
        print("Your ticket price is $5")
        ticket_price = 5
    else:
        print("Please pay $7")
        ticket_price = 7
        
    want_photo = input("Do you want to have a photo taken? Type y for Yes and n for No.")  
    if want_photo == "y":
        print(f"Your total price will be : {ticket_price + 3}") 
    else:
        print(f"Your total price will be : {ticket_price}")
else:
    print("Not eligible")