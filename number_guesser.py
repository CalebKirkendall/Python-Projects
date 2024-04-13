import numpy as np

def random_number():
    return np.random.randint(0,10)

def guess_test(num,ans):
    if num < 0 or num > 10:
        print("WARNING: The machine's integer is between 0 and 10, therefore your guess could not possibly be correct and will provide no value to you.")
        return False
    if num > ans:
        print("The random number is less than your guess, enter a new guess.")
        return False
    elif num < ans:
        print("The random number is greater than your guess, enter a new guess.")
        return False
    else:
        print("You guessed the machine's random integer correctly. Good work.")
        return True
    
def random_number_game():
    answer = random_number()
    attempts = 1
    print("The machine has chosen a random integer ranging from 0 and 10. Take a guess at the integer.\nEnter your guess: ")
    guess_str = input()
    guess_num = int(guess_str)

    while not guess_test(guess_num,answer):
        attempts += 1
        guess_str = input()
        guess_num = int(guess_str)
    if attempts == 1:
        print("You successfully guessed the integer with only " + str(attempts) + " attempt")
    else:
        print("You successfully guessed the integer after " +  str(attempts) + " attempts")

random_number_game()
print("Would you like to play again? y/n")
again = input()
while again == "y":
    random_number_game()
    print("Would you like to play again? y/n")
    again = input()
print("\n\nThanks for playing!")

