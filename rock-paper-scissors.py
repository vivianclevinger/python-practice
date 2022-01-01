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

# Print statement welcomes user to the game
print("Welcome to the Rock Paper Scissors game!")

# Creating this game, I ran into a problem with validating user input because my code uses indices and I ran into Index Errors when testing invalid input. To solve this, I used exception handling with try/except.
try:
  user_num = int(input("What do you choose? Type 0 for Rock, 1 for Paper, and 2 for Scissors.\n"))

# Variable storing list of possible choices
  choices = ["Rock", "Paper", "Scissors"]

# Variable storing random generated integer between 0 and 2. 
  computer_num = random.randint(0, 2)

# Below are nested if-elif statements that output different outcomes depending on computer's choice and user's choice. I would like to work on this again in the future so I can reduce the need for multiple if-elif statements, because the solution for this project was shown to have less code. 

  if choices[computer_num] == "Rock":
    if choices[user_num] == "Rock":
      print(f"You chose: {rock} \nComputer chose: {rock}\nThere was a tie!")
    elif choices[user_num] == "Paper":
      print(f"You chose: {paper}\nComputer chose: {rock}\nYou win!")
    elif choices[user_num] == "Scissors":
      print(f"You chose: {scissors}\nComputer  chose: {rock}\nYou lose!")

  if choices[computer_num] == "Paper":
    if choices[user_num] == "Rock":
      print(f"You chose: {rock} \nComputer chose: {paper}\nYou lose!")
    elif choices[user_num] == "Paper":
      print(f"You chose: {paper}\nComputer chose: {paper}\nThere was a tie!")
    elif choices[user_num] == "Scissors":
      print(f"You chose: {scissors}\nComputer chose: {paper}\nYou win!")

  if choices[computer_num] == "Scissors":
    if choices[user_num] == "Rock":
      print(f"You chose: {rock}\nComputer chose: {scissors}\nYou win!")
    elif choices[user_num] == "Paper":
      print(f"You chose: {paper}\nComputer chose: {rock}\nYou lose!")
    elif choices[user_num] == "Scissors":
      print(f"You chose: {scissors}\nComputer chose: {scissors}\nThere was a tie!")

# Below is the message that outputs when an Index error occurs. I did not account for negative numbers, so I will have to fix that in the future.
except IndexError:
  print("Invalid input! Please try again!")
