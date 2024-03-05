import random

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

player_choose = input(print("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
player_choose = int()

if player_choose == 0:
  print(f"You chose Rock {rock}")
elif player_choose == 1:
  print(f"You chose Paper {paper}")
elif player_choose == 2:
  print(f"You chose Scissors {scissors}")
else:
  print("Invalid choice. Please enter 0, 1, or 2.")

computer_choice = random.randint(0,2)

if computer_choice == 0:
  print(f"Computer chose: {rock}")
elif computer_choice == 1:
  print(f"Computer chose: {paper}")
else:
  print(f"Computer chose: {scissors}")

if player_choose == computer_choice:
  print("It's a draw")
elif player_choose == 0 and computer_choice == 1:
  print("Computer wins")
elif player_choose == 0 and computer_choice == 2:
  print("You win :)")
elif player_choose == 1 and computer_choice == 0:
  print("You win :)")
elif player_choose == 1 and computer_choice == 2:
  print("Computer wins")
elif player_choose == 2 and computer_choice == 0:
  print("Computer wins")
elif player_choose == 2 and computer_choice == 1:
  print("You win :)")