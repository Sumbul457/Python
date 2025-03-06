from random import randint

Computer = randint(1, 100)
guesses = 0

while True:
    guesses += 1
    User = int(input("Enter a number: "))

    if User > Computer:
        print("Enter a smaller number:")
    elif User < Computer:
        print("Enter a higher number:")
    else:  
        print("You guessed the right number:", Computer)
        break

print(f"You guessed the number in {guesses} guesses")
