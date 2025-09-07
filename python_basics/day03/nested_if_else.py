print("Welcome to the rollercoaster!")
height = int(input("What is you height in cm? "))

if height > 120:
    age = int(input("You are eligible for rollercoaster ride, what is your age? "))
    if age > 18:
        print("Your ticket price is $12.")
    elif age < 12:
        print("Your ticket price is $5")
    elif age > 45 and age < 56:
        print("You can ride for free")
    else:
        print("Please pay $7")
else:
    print("Not eligible")