import random

# Define the deck of cards
suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
ranks = [
    "Two",
    "Three",
    "Four",
    "Five",
    "Six",
    "Seven",
    "Eight",
    "Nine",
    "Ten",
    "Jack",
    "Queen",
    "King",
    "Ace",
]

# Create a dictionary to map card ranks to their values
card_values = {
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5,
    "Six": 6,
    "Seven": 7,
    "Eight": 8,
    "Nine": 9,
    "Ten": 10,
    "Jack": 10,
    "Queen": 10,
    "King": 10,
    "Ace": 11,
}


# Function to create a deck of cards
def create_deck():
    deck = []
    for suit in suits:
        for rank in ranks:
            deck.append(f"{rank} of {suit}")
    random.shuffle(deck)
    return deck


# Function to calculate the total value of a hand
def calculate_hand_value(hand):
    value = 0
    aces = 0
    for card in hand:
        rank = card.split()[0]
        value += card_values[rank]
        if rank == "Ace":
            aces += 1
    while aces > 0 and value > 21:
        value -= 10
        aces -= 1
    return value


# Initialize the game
deck = create_deck()
player_hand = [deck.pop(), deck.pop()]
dealer_hand = [deck.pop(), deck.pop()]

print("Welcome to Blackjack!")

# Player's turn
while True:
    player_value = calculate_hand_value(player_hand)
    print(f"Your hand: {', '.join(player_hand)}")
    print(f"Your hand value: {player_value}")

    if player_value == 21:
        print("Blackjack! You win!")
        break
    elif player_value > 21:
        print("Bust! You lose.")
        break

    action = input("Do you want to 'hit' or 'stand'? ").lower()
    if action == "hit":
        player_hand.append(deck.pop())
    elif action == "stand":
        break
    else:
        print("Invalid input. Please enter 'hit' or 'stand'.")

# Dealer's turn
while calculate_hand_value(dealer_hand) < 17:
    dealer_hand.append(deck.pop())

dealer_value = calculate_hand_value(dealer_hand)
print(f"\nDealer's hand: {', '.join(dealer_hand)}")
print(f"Dealer's hand value: {dealer_value}")

# Determine the winner
if dealer_value > 21:
    print("Dealer busts. You win!")
elif player_value > dealer_value:
    print("You win!")
elif player_value < dealer_value:
    print("Dealer wins.")
else:
    print("It's a push (tie).")

print("Thanks for playing!")
