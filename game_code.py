import random

secret_number = random.randint(1, 10)
attempts = 5

print("Welcome to Guess My Number Game")
print("Guess a number between 1 and 10. You have 5 tries.")

while attempts > 0:
    try:
        guess = int(input("Enter your guess: "))
    except ValueError:
        print("Invalid input! Enter a number.")
        continue
    
    attempts -= 1
    
    if guess == secret_number:
        print("You win! Correct answer.")
        break
    elif attempts > 0:
        if guess < secret_number:
            print("Try higher!")
        else:
            print("Try lower!")
        print("Tries left:", attempts)
        print()

if attempts == 0 and guess != secret_number:
    print("Game Over! The number was:", secret_number)
    