import random

# Definindo as representações visuais para pedra, papel e tesoura
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

# Solicita a escolha do jogador
player_choose = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors: "))

# Exibe a escolha do jogador com base na entrada
if player_choose == 0:
    print(f"You chose Rock {rock}")
elif player_choose == 1:
    print(f"You chose Paper {paper}")
elif player_choose == 2:
    print(f"You chose Scissors {scissors}")
else:
    print("Invalid choice. Please enter 0, 1, or 2.")

# Gera a escolha aleatória do computador
computer_choice = random.randint(0, 2)

# Exibe a escolha do computador com base na escolha aleatória
if computer_choice == 0:
    print(f"Computer chose: {rock}")
elif computer_choice == 1:
    print(f"Computer chose: {paper}")
else:
    print(f"Computer chose: {scissors}")

# Verifica o resultado do jogo com base nas escolhas do jogador e do computador
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
