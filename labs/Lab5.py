import datetime
import random

def secondAge():
    while True:
        try:
            bday = input( "please enter your exact date of birth(ex.          February 2 1993 "       )
            birthday = datetime.datetime.strptime(bday, '%B %d %Y')
            break
        except:
            print(" please put in the format ' month day year' without any space")
    tday = datetime.datetime.today()
    timedelta = (tday - birthday).total_seconds()
    print(" you have been alive for ", int(timedelta),"seconds")

secondAge()

def letterVowel(word):
    vowels = ["a","e", "i", "o", "u"]
    vowelCount = 0
    otherCount = 0
    for letters in word:
        if letters.isalpha():
            if letters in vowels:
                vowelCount +=1
            else:
                otherCount +=1

    print(" this word has" + str(len(word)) + "letters" + str(vowelCount) +
         " of which are vowels and "+ str(otherCount) + " are consenants. this word contains" + str(vowelCount + otherCount)) 
word = input(" what word do you want to parse out?: ")
letterVowel(word)

def PrimeNumbers():
    while True:
        try:
            maxNumber = int(input("what is the max number"))
            break
        except:
            print(" this is not a valid number ..")
    def isPrime(num):
        for i in range(2, int(num/2)+1):
            if (num % i) ==0:
                return False

        return True

    count = 0
    for i in range(2,maxNumber+1):
        if isPrime(i):
            count += 1
    print("There are " + str(count) +
            "Prime Numbers between 0 and " + str(maxNumber))
PrimeNumbers()
            
def guessingGame ():
    correctNumber = random.randint(0,100)

    guessing = False
    while True:
        if not guessing:
            guessing == True
            guess = int(input("Guess a number between 0 and 100  "))
            if guess > correctNumber:
                print(" your guess is to High")
                guessing = False
            elif guess < correctNumber:
                print(" your guess is to low!")
                guessing = False
            else:
                print(" you are correct! the number is " + str(correctNumber))
                break
guessingGame()
                 