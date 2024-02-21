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

#Write your code below this line 👇
import random

move = ["Rock", "Paper", "Scissors"]
random_move = random.choice(move)
move_player2 = random_move

move_player1 = int(input("What move do you want to make? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n"))

if move_player1 == 0 and move_player2 == "Rock":
    print("Player 1 chose:")
    print(rock)
    print("Player 2 chose:")
    print(rock)
    print("The result is: Draw")
elif move_player1 == 0 and move_player2 == "Paper":
    print("Player 1 chose:")
    print(rock)
    print("Player 2 chose:")
    print(paper)
    print("The result is: You lose")
elif move_player1 == 0 and move_player2 == "Scissors":
    print("Player 1 chose:")
    print(rock)
    print("Player 2 chose:")
    print(scissors)
    print("The result is: You win!")

if move_player1 == 1 and move_player2 == "Rock":
    print("Player 1 chose:")
    print(paper)
    print("Player 2 chose:")
    print(rock)
    print("The result is: You win!")
elif move_player1 == 1 and move_player2 == "Paper":
    print("Player 1 chose:")
    print(paper)
    print("Player 2 chose:")
    print(paper)
    print("The result is: Draw")
elif move_player1 == 1 and move_player2 == "Scissors":
    print("Player 1 chose:")
    print(paper)
    print("Player 2 chose:")
    print(scissors)
    print("The result is: You lose")

if move_player1 == 2 and move_player2 == "Rock":
    print("Player 1 chose:")
    print(scissors)
    print("Player 2 chose:")
    print(rock)
    print("The result is: You lose")
elif move_player1 == 2 and move_player2 == "Paper":
    print("Player 1 chose:")
    print(scissors)
    print("Player 2 chose:")
    print(paper)
    print("The result is: You win!")
elif move_player1 == 2 and move_player2 == "Scissors":
    print("Player 1 chose:")
    print(scissors)
    print("Player 2 chose:")
    print(scissors)
    print("The result is: Draw")

