import random
wordList = 'dog cow hat bird extraterrestrial undeniable disasterous explosive fortitude alligator crocodile runner wheat foggy vision king loops showered typed untouchable invincible frog pool marshmallow buffet flying envious skeleton cranium'.split()
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

# i = 0
# while i < len(HANGMAN_BOARD):
#     print(HANGMAN_BOARD[i])
#     i += 1

def getRandomWord(wordList):
    pass








