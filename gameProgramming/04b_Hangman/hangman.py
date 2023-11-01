import random
wordList = 'dog cow tortilla bird extraterrestrial undeniable disasterous explosive fortitude alligator crocodile runner wheat foggy vision king loops showered typed untouchable invincible frog pool marshmallow buffet flying envious skeleton cranium gallows'.split()
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

# i = 0
# while i < 500000:
#     getRandomWord(wordList)
#     i += 1

def displayBoard(incorrectLetters, correctLetters , secretWord):
    print(HANGMAN_BOARD[len(incorrectLetters)])
    print()






















