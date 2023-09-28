import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

hand_signs = [rock, paper, scissors]

user_choice = int(input("select 0 for rock, 1 for papper, 2 for scissor \n"))
print(hand_signs[user_choice])
computer_choose = random.randint(0, 2)
print(f"computer choose {computer_choose}")
print(hand_signs[computer_choose])


if user_choice > 3 or user_choice < 0:
    print("Invalid Number! You Lose")
elif user_choice == 0 and computer_choose == 1:
    print("You Lose!")
elif user_choice == 1 and computer_choose == 0:
    print("You Win")
elif user_choice == 0 and computer_choose == 2:
    print("You Win")
elif user_choice == 2 and computer_choose == 0:
    print("You Lose")
elif user_choice == 1 and computer_choose == 2:
    print("You Lose")
elif user_choice == 2 and computer_choose == 1:
    print("You Win")
elif user_choice == computer_choose:
    print("It's a tie!")
