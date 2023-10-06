# import random

# word_list = ["shahed", "hossain", "trishan"]
# display = []
# chosen_word = random.choice(word_list)
# word_length = len(chosen_word)
# guess = input("Guess a letter, ").lower()

# for _ in range(word_length):
#     display += "_"

# guess = input("Guess a letter: ").lower()


# for letter in chosen_word:
#     if letter == guess:
#         print("Match")
#     else:
#         print("Not a match")

# Step 2

import random

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)


print(f"Pssst, the solution is {chosen_word}.")

display = []
word_length = len(chosen_word)
for _ in range(word_length):
    display += "_"

guess = input("Guess a letter: ").lower()


for position in range(word_length):
    letter = chosen_word[position]

    if letter == guess:
        display[position] = letter


print(display)
