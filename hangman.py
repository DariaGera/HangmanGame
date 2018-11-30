# Problem Set 2, hangman.py
# Name:Daria Gerasymchuk KM-82 
# Collaborators:Daria Tymoshenko KM-82
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    k=0
    for el in secret_word:   
        k=0
        for e in letters_guessed: 
            if el!= e:	
                k+=1
    if k==len(letters_guessed):
        return False
    else:
        return True



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    k=0
    for el in secret_word:   
        k=0
        for e in letters_guessed: 
            if el!= e:	
                k+=1
                if k==len(letters_guessed):
                    secret_word=secret_word.replace(el,'_ ')
    return secret_word



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    
    strng=string.ascii_lowercase
    for el in letters_guessed:
        strng=strng.replace(el,"")
    return strng
    
    

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    print('-' * 40)
    lives = 6
    tries = 3
    letters_guessed = []
    k = 0
    print('Hello, you are in the game Hangman now!')
    print('Computer is thinking of a word that is %s letters long.' %len(secret_word))
    print('_ '*len(secret_word))
	
    while lives > 0:
        print('Now you have %s lives' %lives)
        print('Available letters: ',get_available_letters(letters_guessed))
        letter = input("Please guess a letter:")
        letter = letter.lower() 
        if not letter.isalpha():
            if tries > 0:
                tries = tries - 1
                print('Oops, it is not a letter, you have %s tries' %tries)
            elif tries <= 0:
                lives = lives - 1
                print('Hey, you have lost all your tries and one life, now you have %s lives!' %lives)
        if letter in letters_guessed:
            if tries > 0:
                tries = tries - 1
                print('This letter is already used, you have %s tries' %tries)
            elif tries <= 0:
                lives = lives - 1
                print('Hey, you have lost all your tries and one life, now you have %s lives!' %lives)
        else:
            letters_guessed.append(letter) 
            get_available_letters(letters_guessed)   
            if letter in secret_word: 
                get_guessed_word(secret_word, letters_guessed)
                print('Yea, this letter is in the word: ',get_guessed_word(secret_word, letters_guessed))
                if letter in letters_guessed:
                    k += 1
                    if k == len(set(secret_word)):
                        score = lives * len(set(secret_word))	
                        print('Congratulations, you won (^-^)!')
                        print('Your total score is {0}!'.format(score))
                        break
            else:
                print('Oops! This letter is not in the word.')
				
                if letter in ["a", "e", "i", "o", "u"]:
                    lives = lives - 2
                    print('You have %s lives, secret_word: ' %lives, get_guessed_word(secret_word, letters_guessed))
                else:
                    lives = lives - 1
                    print('You have %s lives, secret_word: ' %lives, get_guessed_word(secret_word, letters_guessed))
				
                if lives <= 0:
                    print("You lose.",secret_word)
					
        print('-' * 40)               
			
    if lives <= 0:
        print('You have no lives (~_~;) The word was %s.' %secret_word)
        



# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    my_word = my_word.replace("_ ", "+")
    if len(my_word) == len(other_word):
        for i in range(len(my_word)):
            if my_word[i] != "+" and my_word[i] != other_word[i]:
                return False
            elif my_word[i] == "+" and other_word[i] in my_word:
                return False
        return True        
    else:
        return False        	 



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    my_word = my_word.replace("_ ", "+")
    possible_matches = []
    for other_word in wordlist:
        if match_with_gaps(my_word, other_word) == True:
            possible_matches.append(other_word)
    if len(possible_matches) == 0:
        return "No matches found"
    else:
        return " ".join(possible_matches)       



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    print('-' * 40)
    lives = 6
    tries = 3
    letters_guessed = []
    k = 0
    print('Hello, you are in the game Hangman now!')
    print('Computer is thinking of a word that is %s letters long.' %len(secret_word))
    print('_ '*len(secret_word))
	
    while lives > 0:
        print('Now you have %s lives' %lives)
        print('Available letters: ',get_available_letters(letters_guessed))
        letter = input("Please guess a letter:")
        letter = letter.lower() 
        if not letter.isalpha() and letter != "*":
            if tries > 0:
                tries = tries - 1
                print('Oops, it is not a letter, you have %s tries' %tries)
            elif tries <= 0:
                lives = lives - 1
                print('Hey, you have lost all your tries and one life, now you have %s lives!' %lives)
        if letter in letters_guessed and letter != "*":
            if tries > 0:
                tries = tries - 1
                print('This letter is already used, you have %s tries' %tries)
            elif tries <= 0:
                lives = lives - 1
                print('Hey, you have lost all your tries and one life, now you have %s lives!' %lives)
        else:
            letters_guessed.append(letter) 
            get_available_letters(letters_guessed)   
            if letter in secret_word: 
                get_guessed_word(secret_word, letters_guessed)
                print('Yea, this letter is in the word: ',get_guessed_word(secret_word, letters_guessed))
                if letter in letters_guessed:
                    k += 1
                    if k == len(set(secret_word)):
                        score = lives * len(set(secret_word))	
                        print('Congratulations, you won (^-^)!')
                        print('Your total score is {0}!'.format(score))
                        break
            else:
                print('Oops! This letter is not in the word.')
				
                if letter in ["a", "e", "i", "o", "u"]:
                    lives = lives - 2
                    print('You have %s lives, secret_word: ' %lives, get_guessed_word(secret_word, letters_guessed))
                elif letter == "*":
                    print("Possible words: ", show_possible_matches(get_guessed_word(secret_word, letters_guessed)))	
                else:
                    lives = lives - 1
                    print('You have %s lives, secret_word: ' %lives, get_guessed_word(secret_word, letters_guessed))
				
                if lives <= 0:
                    print("You lose.",secret_word)
					
        print('-' * 40)               
			
    if lives <= 0:
        print('You have no lives (~_~;) The word was %s.' %secret_word)



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    secret_word = choose_word(wordlist)
    hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    #secret_word = choose_word(wordlist)
    #hangman_with_hints(secret_word)
