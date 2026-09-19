import random

best_attempts = None

while True:
    level = input("Choose difficulty (easy/medium/hard): ").lower()

    if level == "easy":
        maximum = 50
    elif level == "medium":
        maximum = 100
    elif level == "hard":
        maximum = 500
    else:
        print("Invalid level")
        continue

    number = random.randint(1, maximum)
    attempts = 0

    print(f"Guess the number between 1 and {maximum}")

    while True:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < number:
            print("Higher!")
        elif guess > number:
            print("Lower!")
        else:
            print("Correct!")
            print("Attempts:", attempts)
            break

    # Best score
    if best_attempts is None or attempts < best_attempts:
        best_attempts = attempts
        print(" New best score!")

    print("Best attempts:", best_attempts)

    again = input("Play again? (yes/no): ")

    if again.lower() != "yes":
        print("Thanks for playing!")
        break