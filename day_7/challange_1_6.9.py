import random

word_list = ["shahed", "hossain", "trishan"]

chosen_word = random.choice(word_list)

guess = input("Guess a letter, ").lower()

for letter in chosen_word:
    if letter == guess:
        print("Match")
    else:
        print("Not a match")
