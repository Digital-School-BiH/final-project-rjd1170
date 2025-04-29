import random
words = ['python','javascript', 'html', 'css','coding','programmer','function','import']

#Random biranje rijeci iz liste

chosen_word = random.choice (words)
word_display = [ '_' for _ in chosen_word ]
attempts = 10 #broj dozvoljenih pokušaja


print ("Welcome to Hangman!")

while attempts > 0 and '_' in word_display:
    print ("\n" + ' '.join(word_display))
    guess = input("Guess a letter: ").lower()
    if guess in chosen_word:
        for index,letter in enumerate(chosen_word):
            if letter == guess:
             word_display[index] = guess #reveal letter
    else:
        print ("This word does not contain that letter")
        attempts -=1

if '_' not in word_display:
    print ("You guessed the word!")
    print(' ' .join (word_display))
    print ("You survived!")
else:
    print("You lost!")
    
        
