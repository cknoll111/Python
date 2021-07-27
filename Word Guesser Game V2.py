# Word Guesser Game

# Program will store a secret word in a variable from a word bank that the player will try to guess
# On each turn, the user will be prompted to enter a single letter
# If the word does not contain that letter, the player gains a "strike". If they have five strikes, they lose, and the game stops
# If the word does contain that letter, the user is shown the secret word, but every unguessed character is hidden. If they've guessed every letter in the word, they have won the game!

# Import the random module 
import random

#secret word bank
secretWordList = ["CAT", "APPLE", "AUTOMOBILE", "BUILDING", "MICROSOFT"]


#define functions
############################################################################

def getLetter():
  letter = "0"
  
  while (True):
    letter = input("Please enter a letter: ")
    if (len(letter) > 1):
      print("Too many letters! Your guess can only be one letter!")
    else:
      return letter.upper()

def displayWord(secretword,guess):               #there are two arguements for the function; the secret word and the guesses
   
  for letter in secretWord:                      # walk through each letter in the secret word and check if the guessed letter is in the secret word
    if (letter in guess):
      print(letter, end=" ")               #if the guess letter is in the word, print the guess letter
    else:
      print("_", end=" ")                  #if the guess letter is not in the word, print a "_"      

def won (secretWord,guess):         #define the function, also has two arguements; the secret word and the guesses
  UserWon = True                    #set to True per the above note

  for letters in secretWord:        #walk through each letter in the secret word
    if(letters not in guesses):     #if the current letter is not in the guess then change the status of UserWon to false and break the loop
      UserWon = False
      break 

  return UserWon

def getSecretWord():
    value = random.choice(secretWordList)
    return value


############################################################################
#Game Loop




#main loop condition for game
def playGame():
    secretWord = getSecretWord()     #define the secret word
    guesses = []            #create an empty list for the guesses
    strikes = 0             #set the number of strikes to 0
    losecondition = 5       #set the number of strikes it takes to lose the game
    
    while ((not won(secretWord,guesses)) and (strikes < losecondition)):
        guess = getLetter()

        if (guess in secretWord):
            guesses.append(guess)
            displayWord(secretWord,guesses)
        else:
            strikes += 1
            print(f"You have {strikes} strikes. If you get 5, you lose!")

    if (strikes >= losecondition):
        print("You lose!")
    
    else:
        print("You win!")

# Define main() function which drives the game
def main():
  choice = "yes"
  
  while (choice == 'yes'):
    choice = input("Do you want to play a game of Hangman? Type 'yes' or 'no'")
    if (choice == 'yes'):
        playGame()
        
    else:
        print("Goodbye!")
      
    
# runs the game via the main() function
main()