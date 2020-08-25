import random
import time


# Function: generateRandom
# Parameters: none
# Return: none
# Purpose:  Generate random number
def generateRandom():
    num = random.randint(1, 100)
    return num

# Function: guidePlayer
# Parameters: num, guess
# Return: bool
# Purpose: Tell user if guess it too high, low,(return false) or if they won (return true)


def guidePlayer(num, guess):
    if (num > guess):
        print("{} is too low!".format(guess))
        return False
    elif (num < guess):
        print("{} is too high!".format(guess))
        return False
    else:
        print("You win!")
        print("You guessed the random number {}".format(num))
        return True

# Function: playGame
# Parameters: none
# Return: none
# Purpose: Runs guessing game


def playGame():
    choice = 0
    chances = 0
    userGuess = ""
    storedGuesses = []

    print("Generating a random number...")
    for i in range(3):
        print(".......+-%*/")
        time.sleep(3)

    print("Random number generated!")
    randomNum = generateRandom()

    while True:
        choice += 1  # count user guesses
        # Makes sure user enters a valid guess (not repeated as well)
        while True:
            userGuess = input("Guess a number (1-100): ")
            if(userGuess.isnumeric() == True and int(userGuess) <= 100):

                if(userGuess in storedGuesses):
                    print(
                        "You have already guessed {}! Guess a different number.\n".format(userGuess))
                else:
                    storedGuesses.append(userGuess)
                    break
            else:
                print("Please enter a valid input. \n")

        results = guidePlayer(randomNum, int(userGuess))

        if (choice == 10 and results == False):  # Ends round if user loses and prints out guesses
            print("You have run out of chances! The number was {}".format(randomNum))
            print("The numbers you have guessed are {} ".format(
                ','.join(storedGuesses)))
            break
        if(results == True):  # prints out guesses after user won
            print("The numbers you have guessed are {} ".format(
                ','.join(storedGuesses)))
            break
        print("\n")


playAgain = ""
while True:
    print("Welcome to Number Guesser!\nYou have 10 chances to guess the right number.\n" +
          "You will be guided in the right direction towards the number so don't worry!")

    time.sleep(5)
    print("Let's Start!")
    playGame()
    while True:  # Makes sure user enters a valid guess 
        playAgain = input("Would you like to play again? (Y/N): ")
        if(playAgain == "Y" or playAgain == "y"):
            print("\n")
            break
        elif(playAgain == "N" or playAgain == "n"): # Ends game
            print("\n")
            print("Hope to see you again!")
            print("Exiting the game..")
            playAgain = False
            time.sleep(3)
            break
        else:
            print("Please enter a value input.")
            continue
    if(playAgain == False):
        break
