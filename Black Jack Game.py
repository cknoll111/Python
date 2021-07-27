#Assumptions:
# Player 1 will always go first and get all of his/her cards
# Player 2 will always follow Player 1 and have the advantage of knowing Player 1's hand.
# The Ace card will always count as a one (1)
# Import the random module / colorama module
import random

from colorama import init
init()
from colorama import Fore, Back, Style

# Create cards dictionary
cards = {
    "A" : 1,  
    "1" : 1,
    "2" : 2,
    "3" : 3,
    "4" : 4,
    "5" : 5,
    "6" : 6,
    "7" : 7,
    "8" : 8,
    "9" : 9,
    "10": 10,
    "J" : 10,
    "Q" : 10,
    "K" : 10
}

# Create reportScore dictionary
reportScore = "{}"

# Define getCard() function
def getCard():
    card, value = random.choice(list(cards.items()))
    print(f"You draw a {card}!")
    return value

# Define declareWinner() function
def declareWinner(P1,P2):
  if (P1 > P2):
    print(f"{Fore.GREEN} Player 1 is the winner!")
  elif (P2 > P1):
    print(f"{Fore.RED}Player 2 is the winner!")
  else :
    print(f"{Fore.YELLOW}It is a tie!")


############################################################################################################
# define the playHand() function 
def playHand(playerTurn):

    # Initialize the score of the current hand
    currentHand = 0    

    # Print out the playerTurn
    print(f"{Style.RESET_ALL}It is currently {playerTurn}'s turn'")

    # Deal two cards and add the scores
    currentHand = (getCard() + getCard())
    print(currentHand)

    # If the score is 21, display "Blackjack!" and return that score
    if (currentHand == 21):
      print("Blackjack!")
      return currentHand

    # Otherwise determine if the player wants to 'hit' or 'stay'
    else:
        while True:
        
            # Report the current score 
            print(f"Current total is: {currentHand}")

            # Ask if the player wants to hit or stay.  Get the user input.
            hitStay = input("Do you want to hit or stay?")

            # if they 'hit', get a card and add the score to the running total score
            if (hitStay == "hit"):
              currentHand = (currentHand + getCard())
              
            # else if they 'stay' print a blank line and break out of the while loop
            if (hitStay == "stay"):
              print()
              break

            # else if they enter neither 'hit' nor 'stay', display 'Invalid entry' and continue the loop
            elif ((hitStay != "hit") and (hitStay != "stay")):
              print("Invalid entry")

             # If the score is 21, display "Blackjack!" and return that score
            if (currentHand == 21):
                print(f"{Fore.YELLOW}***********Blackjack!*************")
                return currentHand
                      
             # if the score is bigger than 21 display "You bust!" and set score to 0.  Return score.
            elif (currentHand > 21):
              print(f"{Fore.RED}you bust!")
              currentHand = 0
              return currentHand

    # return the final score of the hand  
    return currentHand

############################################################################################################

# Define the playGame() function
def playGame():
  P1Score = 0
  P2Score = 0

  P1Score = playHand("Player 1") 

  P2Score = playHand("Player 2") 

  declareWinner(P1Score,P2Score)


# Define main() function which drives the game
def main():
  choice = "yes"
  
  while (choice == 'yes'):
    choice = input(f"{Style.RESET_ALL} Do you want to play a hand of Blackjack? Type 'yes' or 'no'")
    if (choice == 'yes'):

      playGame()
    else:
      print("Goodbye!")
    
# runs the game via the main() function
main()