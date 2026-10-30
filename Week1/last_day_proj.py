import random

play_again = True
while play_again == True:
    secret_num = random.randint(1, 100)
    guessed_num = 0
    rounds_count = 1
    play_again_input = "YO"

    while guessed_num != secret_num:
        guessed_num = int(input("Guess the number (1-100): "))

        if (guessed_num > 100) or (guessed_num < 1):
            print("Invalid Input, Enter From 1 To 100")
        elif guessed_num > secret_num:
            print("Lower")
            rounds_count += 1
        elif guessed_num < secret_num:
            print("Higher")
            rounds_count += 1

    else:
        print(f"Correct! You got it in {rounds_count} attempts.")
        while (play_again_input != "n") and (play_again_input != "y"):
            play_again_input = input("Play again? (y/n):")
            if play_again_input == "y":
                play_again = True
                break
            elif play_again_input == "n":
                print("Thanks for playing!")
                play_again = False
                break
            else:
                print("Please enter a (y/n)")
