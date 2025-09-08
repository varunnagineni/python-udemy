import random

choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

computer_choice = random.randint(0, 2)
print(computer_choice)

result_lose = "You lose"
result_win = "You win"
result_draw = "Draw!"
if choice == 0:
    if computer_choice == 2:
        print("Computer Choice: Scissors")
        print(result_win)
    elif computer_choice == 0:
        print(result_draw)
    else:
        print(result_lose)
elif choice == 1:
    if computer_choice == 0:
        print("Computer Choice: Rock")
        print(result_win)
    elif computer_choice == 1:
        print(result_draw)
    else:
        print(result_lose)
elif choice == 2:
    if computer_choice == 1:
        print("Computer Choice: Paper")
        print(result_win)
    elif computer_choice == 2:
        print(result_draw)
    else:
        print(result_lose)
else:
    print("Select wrong choice!!!")
    
# Rock wins against Scissors
# Scissors wins against paper
# Paper wins against rock
