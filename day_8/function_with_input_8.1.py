def greet():
    print("Hi, Mom! How are you?\n")
    print("How is your day?\n")
    print("How are you?\n")


greet()

# with input


def greet_with_input(name):
    print(f"Hi, {name}! how are you?")
    print(f"How was your day {name}?")
    print(f"Did you go out today {name}?")


greet_with_input("Mom")

# with more than one input


def name_and_location(name, place):
    print(f"Hello {name} did you to shopping today at {place}?")
    print(f"{name} what did you get from {place}?")


name_and_location("Mom", "BC")
