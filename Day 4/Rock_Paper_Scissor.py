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

possibl = [rock,paper,scissors]
randomplay = random.randint(0,2)
computer = possibl[randomplay]

user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if user_input > 2:
    print("You type an invalid number,You Lose")
else:
    user = possibl[user_input]
    print(user)
    print("Computer chose:")
    print(computer)

    if user_input == 0:
        if randomplay ==0:
            print("Match Draw")
        elif randomplay == 1:
            print("You Lose")
        elif randomplay == 2:
            print("You Win")

    elif user_input == 1:
        if randomplay ==0:
            print("You Win")
        elif randomplay == 1:
            print("Match Draw")
        elif randomplay == 2:
            print("You Lose")

    elif user_input == 2:
        if randomplay ==0:
            print("You Lose")
        elif randomplay == 1:
            print("You Win")
        elif randomplay == 2:
            print("Match Draw")
