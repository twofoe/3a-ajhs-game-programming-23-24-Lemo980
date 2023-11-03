import random
wordList = 'dog cow tortilla bird extraterrestrial undeniable disasterous explosive fortitude alligator symbiosis runner wheat foggy vision king loops showered typed untouchable invincible frog pool marshmallow buffet flying envious skeleton cranium gallows'.split()
#.split() will split a string into seperate elements, by default set to space

#VARIABLE_NAMES that are ALL CAPS are constants and are not meant to change.
HANGMAN_BOARD = ['''
x-----x
      |
      |
      |
      |
      |
 0=========0 ''' , '''
x-----x
O     |
      |
      |
      |
      |
 0=========0 ''' , '''
x-----x
O     |
|     |
      |
      |
      |
 0=========0 ''' , '''
x-----x
O     |
|\    |
      |
      |
      |
 0=========0 ''' , '''
 x-----x
 O     |
/|\    |
       |
       |
       |
  0=========0 ''' , '''
 x-----x
 O     |
/|\    |
  \    |
       |
       |
  0=========0 ''' , '''
 x-----x
 O     |
/|\    |
/ \    |
       |
       |
  0=========0''']

def getRandomWord(wordList):
    wordIndex = random.randint(0 , len(wordList) - 1)
    #len(listName) - 1 is most common way to prevent index out of range errors.
    return wordList[wordIndex]

def displayBoard(missedLetters, correctLetters , secretWord):
    print(HANGMAN_BOARD[len(missedLetters)])
    print()

    #Display incorrect guesses
    print('Missed letters:', end = ' ')
    for letter in missedLetters:
        print(letter, end = ' ')
    print()
    
    blanks = ' ' * len(secretWord)
    for i in range(len(secretWord)):
          if secretWord[i] in correctLetters:
               blanks = blanks[:i] + secretWord[i] + blanks[i+1:]
               # the : character is used to slice things into pieces
               #[:i] means slice from the start until index i
               #[i+1:] means slice from i+1 to the end
               #[startingPoint:endingPoint]
    for letter in blanks:
          print(letter, end = ' ')
    print()
     
def getGuess(alreadyGuessed):
    #Only allow: single character, A-Z only, hasnt been guessed
     while True:
          print('Please guess a letter and press enter')
          guess = input().lower()
          if len(guess) != 1:
               print('Please enter a single letter. \n')
          elif guess not in "abcdefghijklmnopqrstuvwxyz":
               print("Please enter an English letter only")
          elif guess in alreadyGuessed:
               print("This letter has already been guessed. Please enter a different letter")
          else:
               return guess

def playAgain():
    print("Would you like to play again? Type yes or no then press enter.")
    return input().lower().startswith('y') # return true or false based on input
               





















