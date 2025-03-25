import random

# Basic Settings
warnings = ["first warning", "second warning", "death"]
word_list = ["anacOnda", "doG", "cat", "chiuAvava", "snake", "sloth"]
alphabet = "abcdefghijklmnopqrstuvwxyz"
playerGuess = ""
guessedLetters = ""
allLetters = ""
false_tries = 0
max_tries = 3

# Returns random word
def randomWord(wordList):
    random_word = (wordList[random.randint(0, len(wordList) - 1)]).lower()
    print(f"DEBUG | randomly chosen word: {random_word}")
    return random_word

# Make player guess
def guessLetter():
    global allLetters, alphabet
    
    while True:
        guess = input("Guess a letter: ")

        if guess in allLetters:
            print(f"You already guessed: {guess}")

        elif len(guess) == 1 and guess.isalpha():
            #print("DEBUG | Correct form")
            break

        elif len(guess) > 1:
            print("only one character!")

        else:
            #print("DEBUG | Wrong form")
            print(f"Guess is not from alphabet!")

    return guess.lower()

# Check Validity of a guess
def isGuessValid(players_guess, random_word):
    global false_tries, guessedLetters, allLetters

    allLetters += players_guess

    if players_guess in random_word:
        guessedLetters += players_guess
        return True
    else:
        false_tries += 1
        
        if false_tries > max_tries:
            print("Exceeded number of tries!")
            return "gameover"
        else:
            #print(f"did not exceed limit tries: {false_tries}, limit: {max_tries}")
            #print(warnings[(false_tries - 1)])
            return False

def board(random_word):
    global guessedLetters
    underscore = ""

    for letter in random_word:
        if letter in guessedLetters:
            underscore += " " + letter
        else:
            underscore += " _ "
    
    print(underscore)

def hasWon():
    global false_tries, max_tries, guessedLetters, random_word

    for letter in random_word:
        if letter in guessedLetters:
            #print(f"{letter} is there")
            None
        else:
            #print(f"Still missing: {letter} there!")
            return False
    return True

random_word = randomWord(word_list)

while True:
    board(random_word)
    players_guess = guessLetter()
    isValid = isGuessValid(players_guess, random_word)
    if isValid != "gameover":
        hasPlayerWon = hasWon()
        
        if hasPlayerWon == True:
            print("PlayerHasWon!")
            break
        else:
            print(f"Wrong Tries: {false_tries}/{max_tries} | All letters: {allLetters} | Correct letters: {guessedLetters}")
    else:
        print("Lost")
        break