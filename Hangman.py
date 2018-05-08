#  AUTHOR:  Michael O'Brien
#  CREATED:  05 April 2018
#  MODIFIED:  08 May 2018
#  DESCRIPTION:  Monty Python hangman game


#  HANGMAN INSTRUCTIONS FUNCTION
def hangmanInstructions():
    instructions = open('hangman_instructions.txt', 'r')
    hangmanInstructions = instructions.read()
    print(hangmanInstructions)
    instructions.close()
    hangmanGame()


#  HANGMAN GAME FUNCTION
def hangmanGame():
    hangmanPics = [
        '''
              +---+
              |   |
                  |
                  |
                  |
                  |
             =========''', '''

           +---+
           |   |
           O   |
               |
               |
               |
         =========''', '''

           +---+
           |   |
           O   |
           |   |
               |
               |
         =========''', '''

           +---+
           |   |
           O   |
          /|   |
               |
               |
         =========''', '''

           +---+
           |   |
           O   |
          /|\  |
               |
               |
         =========''', '''

           +---+
           |   |
           O   |
          /|\  |
          /    |
               |
         =========''', '''

           +---+
           |   |
           O   |
          /|\  |
          / \  |
               |
         ========='''
    ]

    import random
    words = ("CAMELOT", "ROBIN", "MINSTREL", "BRING OUT YER DEAD", "THE MEANING OF LIFE", "SIR GALAHAD", "THE LIFE OF BRIAN", "CASTLE", "SIR BEDEVERE", "BROTHER MAYNARD", "HOLY GRAIL", "MONTY PYTHON", "KING ARTHUR", "FLYING CIRCUS", "SIR LANCELOT", "BLACK KNIGHT", "LUMBERJACK")
    print('H A N G M A N')
    missedLetters = ''
    correctLetters = ''
    secretWord = random.choice(words)
    gameIsOver = False

    while True:
        displayBoard(hangmanPics, missedLetters, correctLetters, secretWord)
        guess = getGuess(missedLetters + correctLetters)
        if guess in secretWord:
            correctLetters = correctLetters + guess
            foundAllLetters = True
            for i in range(len(secretWord)):
                if secretWord[i] not in correctLetters:
                    foundAllLetters = False
                    break
            if foundAllLetters:
                print('Yes!  The secret word was ' + secretWord + '.  You win.')
                gameIsOver = True
        else:
            missedLetters = missedLetters + guess
            if len(missedLetters) == len(hangmanPics) - 1:
                displayBoard(hangmanPics, missedLetters, correctLetters, secretWord)
                print('You are out of guesses.  The secret word was ' + secretWord + '.  Sorry, you lose.')
                gameIsOver = True
        if gameIsOver:
            if playAgain():
                hangmanGame()
            else:
                print('I hope you enjoyed Monty Python Hangman.')


#  DISPLAY THE BOARD FUNCTION
def displayBoard(hangmanPics, missedLetters, correctLetters, secretWord):
    print(hangmanPics[len(missedLetters)])
    print()
    print('Missed Letters:  ')
    for letter in missedLetters:
        print(letter, end=" ")
    print()
    blanks = '_' * len(secretWord)
    for i in range(len(secretWord)):
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i + 1:]
    for letter in blanks:
        print(letter, end=' ')
    print()


#  GET GUESS FUNCTION - CHECKS TO MAKE SURE INPUT IS A SINGLE LETTER
def getGuess(alreadyGuessed):
    while True:
        guess = input('Guess a letter:  ')
        guess = guess.upper()
        if len(guess) != 1:
            print('Please enter a single letter.')
        elif guess in alreadyGuessed:
            print('You have already guessed that letter.  Choose again.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ':
            print('Please enter only letters.')
        else:
            return guess


#  PLAY AGAIN FUNCTION
def playAgain():
    print()
    print('Do you want to play again?  (Yes/No)  ')
    return input().lower().startswith('y')


hangmanInstructions()
