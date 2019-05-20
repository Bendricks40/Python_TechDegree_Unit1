"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------
For this first project we will be using Workspaces.
NOTE: If you strongly prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.
"""

import random

best_score = 9999999


def start_game(score):
    """Psuedo-code Hints
    When the program starts, we want to:
    ------------------------------------
    1. Display an intro/welcome message to the player.
    2. Store a random number as the answer/solution.
    3. Continuously prompt the player for a guess.
      a. If the guess greater than the solution, display to the player "It's lower".
      b. If the guess is less than the solution, display to the player "It's higher".
    4. Once the guess is correct, stop looping, inform the user they "Got it"
         and show how many attempts it took them to get the correct number.
    5. Let the player know the game is ending, or something that indicates the game is over.
    ( You can add more features/enhancements if you'd like to. )
    """
    # write your code inside this function.

    top_score = score

    print("\n***************************************************"
          "\n    Welcome to the world's best guessing game!!    ")
    if top_score < 9999999:
        print("    High Score: {}   <--- Can you beat this?!?!?     ".format(top_score))
    print("***************************************************")
    print("\n\nBegin the game below by entering your first guess between 1 and 10: ")

    solution = random.randint(1, 10)
    user_answer = 15
    valid_guess_count = 0

    while user_answer != solution:

        try:
            user_answer = int(input("\nEnter a guess: "))
            while user_answer > 10 or user_answer < 1:
                user_answer = int(input("\nOops, that's not a valid guess. Enter a valid guess between 1 and 10: "))
            valid_guess_count += 1
            if user_answer > solution:
                print("\nNice try, but that guess is HIGHER than the solution. "
                      "Try again! Total guess count so far: {} ".format(valid_guess_count))
            elif user_answer < solution:
                print("\nNice try, but that guess is LOWER than the solution. "
                      "Try again! Total guess count so far: {}".format(valid_guess_count))
            elif user_answer == solution and valid_guess_count > 1:
                print("Excellent!! You have guessed correctly!! {} is indeed the correct answer, "
                      "and it took you {} guesses".format(user_answer, valid_guess_count))
                if valid_guess_count < top_score:
                    top_score = valid_guess_count
                play_again = input("\nWould you like to play again? (y/n): ")
                if play_again == "y":
                    start_game(top_score)
                elif play_again != "y":
                    print("\nThanks for playing! \n")

            elif user_answer == solution and valid_guess_count == 1:
                print("WOW!!! Telepathy runs deep with you I see. "
                      "{} is indeed the correct answer, and it only took you 1 try. Amazing!!".format(user_answer))
                top_score = 1
                play_again = input("\nWould you like to play again? (y/n): ")
                if play_again == "y":
                    start_game(top_score)
                elif play_again != "y":
                    print("\nThanks for playing! \n")
        except ValueError as e:
            print("Not a valid integer. Please try again! \n\n(For my fellow nerds, here is the error message: {})".format(e))


if __name__ == '__main__':
    # Kick off the program by calling the start_game function.

    start_game(best_score)

