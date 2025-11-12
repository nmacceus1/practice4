import random
print("Welcome to Rock-Paper-Scissors!")
choice = random.randint(1, 3)
if (choice == 1):
    strchoice = "rock"
elif (choice == 2):
    strchoice = "paper"
elif (choice == 3):
    strchoice = "scissors"

print(f"Computer chose: {strchoice}")
