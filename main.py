rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random

rps_choice = [rock, paper, scissors]
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))

if user_choice < 3 and user_choice > -1:
	print(rps_choice[user_choice])


	computer_choice = random.randint(0, 2)
	print(f"Computer chose {computer_choice}")
	print(rps_choice[computer_choice])
	
	
	
	if user_choice == 0 and computer_choice == 2:
		print("You win")
	elif user_choice == 2 and computer_choice == 0:
		print("You lose")
	elif user_choice > computer_choice and user_choice < 3:
		print("You win")
	elif computer_choice > user_choice and user_choice > -1:
		print("You lose")
	elif computer_choice == user_choice:
		print("Draw")
	else: 
		print("You typed an invalid number. You lose!")	
else: 
	print("You typed an invalid number! You lose")


