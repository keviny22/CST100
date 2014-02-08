#In this Assignment you are going to program a number guessing game. Using a loop is not necessary to complete the assignment,
#however it can make the code much easier to read rather than using nested IF statements.
#
#Using the nested IF statements approach, the following steps need to be performed:
#
#1. Initialize a variable called number with a value of 10 and a variable called numAttempts with a value of 0
#
#2. Ask the user for their name
#
#3. Ask the user to guess a number between 1 and 20 and store that in a variable guess, increment the numAttempts variable
#
#4. If guess is same as number then say your guess is correct and you guessed it in n attempt(s), where n is the value of numAttempts variable and your program ends.
#
#5. If guess is lower than number then print "Your guess is too low". If numAttempts variable < 3, the goto step #7 else goto step #8.
#
#6. If guess is higher than number then print "Your guess is too high". If numAttempts variable < 3, the goto step #7 else goto step #8 
#
#7. Repeat step #3 - #6.
#
#8. If the user does not guess the number even after three attempts then print ?Your three guesses are over, the number I was thinking of was 10?
#
#
#Sample 1
#
#Hello! What is your name?
#Albert
#Well, Albert, I am thinking of a number between 1 and 20.
#Take a guess.
#15
#Your guess is too high.
#Take a guess.
#4
#Your guess is too low.
#Take a guess.
#12
#Your guess is too high. Your three guesses are over.  The number I was thinking of was 10
#
#Sample 2
#
#Hello! What is your name?
#Albert
#Well, Albert, I am thinking of a number between 1 and 20.
#Take a guess.
#8
#Your guess is too low.
#Take a guess.
#12
#Your guess is too high.
#Take a guess.
#10
#Good job, Albert! You guessed my number in 3 guesses!
#
#
#Optional: Instead of fixing the number to be guessed to 10, you can initialize 'number' variable with a random number between 1 and 20 that you generate using the functions in the random module.
#This way every time you re run the program, it is a different number to be guessed. 


number = 10
numAttempts = 0
numMaxAttempts = 3

def guess(int_guess):
    if int_guess > number:
        print("Your guess is too high.")
    elif int_guess < number:
        print("Your guess is too low.")
    elif int_guess == number:
        print("Good job, " + str_name + "! You guessed my number in " + str(numAttempts) + " guesses!")
        exit()

str_name = input("Hello! What is your name?\n")
print("Well, " + str_name + ", I am thinking of a number between 1 and 20.")

while numAttempts < numMaxAttempts:
    numAttempts += 1
    guess(int(input("Take a guess.\n")))
else:
    print("Your three guesses are over. The number I was thinking of was " + str(number))
    



    
