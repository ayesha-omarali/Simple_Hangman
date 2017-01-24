'''
Ayesha Omarali
This is a command line game for hangman!
'''
print('Welcome to the hangman game! Command line style!')

archived_guesses = set()

#2. TOOL FOR RANDOMLY SELECTING WORD
from random import randint

#1. READ WORD POOL AND CREATE WORD LIST
with open('word_list.txt', 'r') as wordlist:
    words = wordlist.read()
wordlist.close()
words = words.split()

#2. RANDOMLY SELECT WORD
i = randint(0, len(words)-1)
word = words[i]

#3. CREATE DASHES TO GUESS FROM
display = ['_']*len(word) #LIST FOR DISPLAY
print(" ".join(str(e) for e in display)) #DASHES
k = 6

while '_' in display:
    if k == 0:
        print("Sorry, you're out of guesses =[")
        break
    #4. ASK FOR GUESS
    guessed_letter = input("What is your next guess? ").lower()
    if guessed_letter in archived_guesses:
        print("Sorry, you already guessed that!")
    elif not guessed_letter.isalpha() or len(guessed_letter)!= 1:
        print("Sorry, that's not a valid guess! It needs to be a letter and only one input")
        k = k - 1
    #5. EVAL GUESS
    elif guessed_letter not in word:
        archived_guesses.update(guessed_letter)
        print("Oops sorry! That's not in the word")
        k = k - 1
    else:
        archived_guesses.update(guessed_letter)
        letters = list(word)
        indices = [i for i, x in enumerate(letters) if x == guessed_letter]
        for i in indices:
            display[i] = guessed_letter
        print("Great job! Here's the updated word with your guess!")
        print(" ".join(str(e) for e in display)) #DASHES
    print("You have {} guesses left".format(k))
#6. FINISHED
if '_' in display:
    print("Sorry you lost =[ thanks for playing! Here's the word! {}".format(word))
else:
    print("Congrats you won!")
