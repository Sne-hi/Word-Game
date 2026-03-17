import random
word_bank = ['rizz','ohio','sigma','based','cringe','sus','yeet','vibe','flex','ghost','lit','salty','slaps','cap','no cap','bet','fam','savage','woke','clout','drip']
word = random.choice(word_bank)
guessedWord = ['_'] * len(word)
attempts = 6
while attempts > 0:
    while attempts >0:
        print("\nCurrent word: " + ' '.join(guessedWord))
        guess = input('Guess a letter: ').lower()
        if guess in word:
            for i in range(len(word)):
                if word[i] == guess:
                    guessedWord[i] = guess
            print(f'Good guess! "{guess}" is in the word.')
        else:
            attempts -= 1
            print(f'Sorry, "{guess}" is not in the word. Attempts left: {attempts}') 
        if '_' not in guessedWord:
            print("\nCongratulations! You've guessed the word: " + word)
            break
        if attempts == 0 and '_' in guessedWord:
            print("\nGame Over! The word was: " + word)
            break
        