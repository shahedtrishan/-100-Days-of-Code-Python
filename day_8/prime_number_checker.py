def prime_number(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print(f"{number} is prime number")
    else:
        print(f"{number} is not prime")


n = int(input("Enter the Number: "))
prime_number(number=n)
