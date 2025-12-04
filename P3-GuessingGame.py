#Guessing Game
guess = 27
attempts = 0
while True:
    num = int(input("Enter your guess:"))
    attempts += 1
    if num==guess:
        print("Congratulations! You guessed it right.")
        print("You took",attempts,"attempts to guess the number.")
        break
    elif guess < num:
        print("Too high")
    else:
        print("Too Low")