import wordle
from words import words
import random


def filter_word_list(words, clues):
    """ This function filters words list based on clues received """
    if not clues:
        return words
    guess, clue_list = clues[-1]
    results = []
    for word in words:
        # get the clues for the current word based on latest guess
        temp_clue_list = wordle.check_word(guess, word.upper())
        green_clues = 0
        all_clues = True # keeps track on true or false
        for i in range(len(clue_list)):
            if temp_clue_list[i] == 'green':
                green_clues += 1
            if clue_list[i] not in temp_clue_list:
                all_clues = False
                break
        green_clue_count = 0
        for clue in clue_list:
            if clue == 'green':
                green_clue_count += 1
        if green_clues == green_clue_count and all_clues:
            new_words = filter_word_list([word], clues[:-1])
            results.extend(new_words)

    if len(results) > 5:
        short_list = random.sample(results, 5)
        short_list = sorted(short_list)
        for i in range(0, 5):
            print(short_list[i])
    else:
        for i in range(len(results)):
            print(results[i])

    return results

if __name__ == "__main__":
    word_list = words
    guesses = 0
    record = []
    clues = []  # this was outside the while loop
    secrets = random.choice(words).upper()
    while guesses < 6:
        guess = input("> ")
        guess = guess.upper()

        if guess.lower() not in words or len(guess) != 5:
            continue
        else:
            temp_clues = guess, wordle.display_wordle(secrets, guess)
            clues.append(temp_clues)
            #filter the word list based on the clues received so far
            word_list = filter_word_list(word_list, clues)


            if guess == secrets:# if guess matches the secret word, break the loop
                break
            else:
                guesses += 1

    print("The secret word was: ", secrets)