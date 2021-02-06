import random
import art

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def check_answer(guess, answer, turns):
    """ Check Guess And Returns The Outcomes. """
    if guess > answer:
        print("Too High...")
        return turns - 1
    elif guess < answer:
        print("Too Low...")
        return turns - 1
    else:
        print(f"You Got It! The Answer Was: {answer}")

def set_difficulty():
    level = input("Choose A Difficulty Level: Type 'easy' Or 'hard':\n")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

def game():
    print(art.logo)
    print("I Am Thinking About A Number Berween 1 and 100 ,..........................................")

    answer = random.randint(1, 100)
    print(f"answer is: {answer}")

    turns = set_difficulty()

    guess = 0
    while guess != answer:
        print(f"You Have {turns} Attempts Remaining To Guess The Number.")

        guess = int(input("Make A Guess:\n"))
        turns = check_answer(guess, answer, turns)

        if turns == 0:
            print(f"You Run Out Of Guesses, You Loose...")
            return
        elif guess != answer:
            print("Guess Again...")
game()