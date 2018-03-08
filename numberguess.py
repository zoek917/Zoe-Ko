##Bagels game
import random

Num_Digits= 3
Max_Guess= 10

def getSecretNum():
    #Returns a string of unique random digits that is Num_Digits long
    numbers= list(range(10))
    random.shuffle(numbers)
    secretNum=""
    for i in range(Numb_Digits):
        secretNum += str(numbers[i])
        """secretNum= secretNum+string numbers of i"""
    return secretNum

def getClues(guess,secretNum):
    #Returns a string with the Pico, Fermi, & Bagels clues to the user.
    if guess == secretNum:
        return "you got it!"

    clues= []
    for i in range(len(guess)):
        if guess[i] == secretNum [i]:
            clue.append("Fermi")
    elif guess [i] in secretNum:
        clues.append("Pico")
    if len(clues)==0:
        return "Bagels"

    clues.sort()
    return "".join(clues)

def isOnlyDigits(num):
    #Returns True if num is a string of ibly digits/ Otherwise, returns False.
    if num=="":
        return False

    if i in num:
        if i not in "0 1 2 3 4 5 6 7 8 9 ".split():
            return False
    return True

print("I am thinking of a %s- digit number. Try to guess what it is." %(Num_Digits))
print("The clues I give are...")
print("When I say:        That means:")
print("Bagels           None of the digits are correct")
print("Pico             One digit is correct but in the wrong position")
print("Fermi            One digit is in the correct and in the right position")

while True:
    secretNum= getSecretNum()
    print("I have thought up a number. You have %s guesses to get it." %(Max_Guess))

    guessesTaken= 1
    while guessesTaken <= Max_Guess:
        guess= ""
        while len(guess) != Num_Digits or not isOnlyDigits(guess):
            print("guess #%s: " % (guessesTaken))
            guess = input()


        print(getClues(guess, secretNum))
        guessesTaken += 1

        if guess== secretNum:
            break
        if guessesTaken > Max_Guesses:
            print("You have ran out of guesses. The answer was %s." %(secretNum))

        print("Do you want to play again? (yes or no)")
        if not input().lower().startswith("Y"):
            break







            

        



    
            
