#Katryn Munoz
#Nov. 14, 2023
#This program will be a coin toss game
#The player gets 10 tries to guess the result of the coin toss

import random
#from random import randint
#from random import *
#from random import randint as r

#return: 1 String for heads or tails
#parameter:none
#This function will return the result of a coin toss
def CoinToss():
    #Simulate the coin toss and return result
    #num=0
    #num = random.randint(1,100)
    #num2= random. randrange(1,101)
    if random.randint(1,2)==1:
        return "heads".capitalize()
    else:
        return "tails".capitalize()

#return: 1 String for guess of Heads or Tails 
#Parameters: 1 String for name
#This function will get a users guess of Heads or tails
def GetGuess(name):
    #Declares and initialize int variable for guess
    userGuess = 0
    
    while userGuess != 1 and userGuess != 2:
        try:
            #Prompt user for guess and validate guess
            print("\n1) Heads\n2) Tails")
            userGuess = int(input(f"Hi {name}, please choose 1 or 2: "))
            if userGuess != 1 and userGuess != 2:
                print(f"Hey {name}, please enter a 1 or 2 only!")
        except:
            print(f"\nYou must type a number {name}!")
            
    #Return guess
    if userGuess==1:
        return "heads".capitalize()
    else:
        return "tails".capitalize()

#Return 1 string win or lose
#Parameter: 1 string for userguess 1 string for coin toss result
#this function determines if user won or loss the coin toss

def WinLose(guess,coin):
    # if user is correct return win, if not lose
    if guess==coin:
        return "win".capitalize()
    else:
        return "lose".capitalize()

#If user guess equals coin toss

def main():
    #Create constant to store 10 available
    TOSSES=10
    #Declare and initialize variables
    #String for user name,user guess, coin toss, play again
    userName = userGuess = coin = result = ""
    playAgain= "yes"
    #Int for score
    score=0
    intro = "Welcome to my coin toss program\n\n"
    #Display Intro
    print(intro.center(50))
    #Prompt user for name
    userName = input("Please enter your name: ").capitalize().strip()
    
    #Loop for play again
    while playAgain == "yes":
        score = 0
        #Loop 10x
        for i in range(TOSSES):
            #Show user round number of total rounds
            print(f"\nRound {i+1} of {TOSSES}\n")
            
            #Prompt for user guess of heads or tails
            userGuess = GetGuess(userName).capitalize()
            #Store result of random coin toss of heads or tails
            coin = CoinToss().capitalize()
            
            #Display correct or not
            result = WinLose(userGuess,coin).capitalize()
            #If user guess equals coin toss
            #Add 1 point to score and tell user they were correct
            #If user guessed wrong tell them they are wrong
            if result== "win".capitalize():
                print("\nYou guessed correctly!")
                score+=1
            else:
                print("\nAwww sorry, you are wrong")
            #Display current score
            print(f"\nAt the end of round {i+1} your score is {score}!")
            
        #Display results of game
        print(f"\nAt the end of your {TOSSES} round game, you scored {score} points!")
        
        #Prompt user to play again
        playAgain = input("Would you like to play again (yes or no)?").strip().lower()
        
    #When user does not want to play anymore display outro
        print(f"Thank you {userName} for playing my game!")

main()

    #NOTES
    #methods
 # .lower() Converts to all lower case
 # .upper () converts to all caps
 # .capitalize()
 # .lstrip()
 # .strip()removes spaces
 # .split()