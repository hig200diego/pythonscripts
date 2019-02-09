#Guess The number new version
import random

guessesTaken = 0 # guessesTaken starts at zero. It will be used in a 'while loop'

random_number = random.randint(1, 20) #generates the random number

myName = input("What´s you name? ")
print("Well, {}, I´m thinking of a number between 1 and 20.".format(myName))

while guessesTaken < 6:
    guess = int(input("Take a guess: "))
    guessesTaken += 1
    
    if guess < random_number:
        print("Your guess is to low")
    
    elif guess > random_number:
        print("Your guess is to high")
        
    else:
        break #This condition is true
        
if guess == random_number:
    print("WELL DONE!!")


if guess != random_number:
    random_number = str(random_number)
    print("Nope. The number I was thinking of was {}.".format(random_number))



