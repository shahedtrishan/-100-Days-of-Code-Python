import math


def paint_calculator(height=4, width=6, cover=5):
    number_of_cans = height * width / cover
    round_cans = math.ceil(number_of_cans)
    print(f"You will need {round_cans} cans of paint")


h = int(input())
w = int(input())
c = 5

paint_calculator(height=h, width=2, cover=c)
