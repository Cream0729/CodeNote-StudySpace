import random

# Get the answer for this game
ans = random.randint(1, 100)

# Set the max times of tried
times = 5

# For tips square
square = random.randint(5, 10)
print("Guess Game start, you will has", times, "times for guesses.\n")

while times > 0:
    guess = int(
        input(f"You have {times} guesses left. Now enter your number(1~100): "))
    if guess == ans:
        print("You guessed right!")
        break
    elif guess > ans:
        if (ans - guess) > square:
            print("You guessed higher!")
        else:
            print("You guessed too higher!")
    elif guess < ans:
        if (ans - guess) < square:
            print("You guessed lower!")
        else:
            print("You guessed too lower!")
    print()
    times -= 1

print("Answer is:", ans, ", square is:", square)
print("Thanks you for playing!")
