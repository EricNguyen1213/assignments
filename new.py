import random
guessed = False
def more_or_less():
    gen_number=random.randint(1,100)
    print("Game started and number generated")
    guessed = False
    while guessed == False:
        guessA = int(input("Player A guess: "))
        guessedIt(guessA, gen_number)
        guessB = int(input("Player B guess: "))
        guessedIt(guessB, gen_number)

def guessedIt(guess, generated):
    if guess > generated:
        print("guess is greater")
    elif guess < generated:
        print("guess is fewer")
    else:
        print("Just right")
        guessed = True
more_or_less()
