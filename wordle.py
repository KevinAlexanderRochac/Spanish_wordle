# Kevin Rochac Cabezas
# 02/20/2023
# Project_1: Latin Wordle


import display_utility
import random
import words
from words import palabras


def create_singlegram(wordss):
    # This singlegram function will be used to create a list of unigrams from the input word

    return [char for char in wordss]


def get_similarity_ratio(word1, word2):
    common = []
    my_string = ""
    single_gram1, single_gram2 = create_singlegram(word1.lower()), create_singlegram(word2.lower())
    # Replace accented characters in single_gram2 with their non-accented equivalents
    accented_chars = {'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u', 'ñ': 'n'}
    single_gram2 = [accented_chars[char] if char in accented_chars else char for char in single_gram2]

    for unigram in single_gram1:
        if unigram in single_gram2:
            common.append(unigram)
    for x in common:
        my_string += x

    return my_string


def autocorrect(input_word, database):
    accented_chars = {'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u', 'ñ': 'n'}

    for x in database.keys():
        last_string = ""
        single_gram = list(x)
        single_gram2 = [accented_chars[char] if char in accented_chars else char for char in single_gram]

        for y in single_gram2:
            last_string += y

        cursim = get_similarity_ratio(input_word, x)

        if cursim == last_string:
            return x

    return None


def check_word(secret, guess):
    """ This function takes in a 5-letter secret word and the 5-letter guess the word
    compares each letter to see if it falls into the green which means the letter is in the word and the right position,
    yellow which means the letter is in the word but in the wrong position or gray meaning it is not in
    the secret word """
    # correct
    new_secret = list(secret)  # converts into a list
    new_guess = list(guess)
    switch = True
    display = []
    for i in range(0, 5):
        if new_secret[i] == new_guess[i]:
            display.append("green")
            new_secret[i] = new_guess[i] = "/"

        elif new_guess[i] in new_secret and guess.count(guess[i]) <= secret.count(guess[i]):
            display.append("yellow")
            new_secret[new_secret.index(new_guess[i])] = "/"  # replaces the character in the index with a "/"

        elif new_guess[i] in new_secret and guess.count(guess[i]) > secret.count(guess[i]) and switch == True:

            same_index = False
            for j in range(0, 5):
                if new_guess[j] == new_secret[j]:
                    same_index = True
            if same_index == False:
                display.append("yellow")
                switch = False
            elif same_index == True:
                display.append("grey")
        else:
            display.append("grey")

    return display


def alternative(clues):  # this hint funtion will display in orange

    """This function will compare the letters that have accent marks
     with the english letters which don't have accent marks, its will
     basically be hinting that a variation of this letter is in the
     secret word."""

    known = []
    new_word = []
    alpha = ''

    for word, clues_list in clues:
        for i in range(len(word)):
            if clues_list[i] == 'orange':
                if word[i] in new_word:
                    if word[i] in known:
                        known.remove(word[i])
                else:
                    known.append(word[i])
            else:
                new_word.append(word[i])

    gamma = sorted(set(known))  # removes duplicates and sorts them alphabetically
    for k in gamma:  # puts the items in the list and converts them into a string
        alpha += k
    return alpha


def known_word(clues):
    """ This function maintains a log of the guesses made and clues received.
    The log will be displayed on the board, indicating letters that are in the word """

    known = ''
    if clues == []:
        return "_____"
    else:
        for i in range(len(clues[-1][0])):
            sigma = ""
            for j in range(len(clues)):
                if clues[j][1][i] == 'green':
                    sigma = clues[j][0][i].upper()
                    break
            if sigma != "":
                known += sigma
            else:
                known += '_'
    return known


def no_letters(clues):
    """This function receives the clues, and its output is a string
    of capitalized letters in alphabetical order that are confirmed to not
    appear in the targeted word"""
    known = []
    new_word = []
    alpha = ''

    for word, clues_list in clues:
        for i in range(len(word)):
            if clues_list[i] == 'grey':
                if word[i] in new_word:
                    if word[i] in known:
                        known.remove(word[i])
                else:
                    known.append(word[i])
            else:
                new_word.append(word[i])

    gamma = sorted(set(known))  # removes duplicates and sorts them alphabetically
    for k in gamma:  # puts the items in the list and converts them into a string
        alpha += k
    return alpha


def yes_letters(clues):
    """This function receives teh clues and its output is a
    string of capitalized letters in alphabetical order that are
    confirmed to appear in the targeted word"""
    # correct
    known = ''
    delta = ''
    for i in range(len(clues)):
        word, clues_list = clues[i]
        for k in range(len(clues_list)):
            if clues_list[k] == 'green':
                known += word[k].upper()
            elif clues_list[k] == 'yellow':
                known += word[k].upper()
            else:
                continue
    x = list(known)  # creates a list
    kappa = list(set(x))  # removes duplicates
    y = sorted(kappa)  # sorts them alphabetically
    for k in y:
        delta += k
    return delta


def display_wordle(secret, guess):
    """ This function makes sure to display certain letters the proper colors
     which are green, yellow, orange and grey"""
    similar_chars = ['Á', 'É', 'Í', 'Ó', 'Ú', 'Ñ']
    clues = []
    for i in range(5):
        if guess[i] == secret[i]:
            display_utility.green(guess[i])
            clues.append("green")
        elif guess[i] in similar_chars and guess[i] in secret:
            display_utility.orange(guess[i])
            clues.append("orange")
        elif guess[i] in secret:
            if guess.count(guess[i]) <= secret.count(guess[i]):
                display_utility.yellow(guess[i])
                clues.append("yellow")
            else:
                display_utility.grey(guess[i])
                clues.append("grey")
        else:
            display_utility.grey(guess[i])
            clues.append("grey")
    print("")
    return clues


# This will be a  new function to get the correction for spanish and/ portugees
# might implement in the (if main) function below

# from autocorrect import Speller
#         spell = Speller(lang= 'es')
#         enter = input("> ").upper()
#         guess = spell(enter)


if __name__ == '__main__':

    item = random.choice(list(words.palabras.items()))
    secret = item[0].upper()
    translation = item[1]

    num_guesses = 0
    clues = []
    green_yellow_clue = []
    orange_clue = []
    grey = []
    updated = '__'
    printer = []
    print("Latin Wordle(Spanish and Portugees)")
    print("These letters might be used -> 'á', 'é', 'í', 'ó', 'ú', 'ñ' ")
    print("Known(Conocido) Letters:_____")  # displays the first part of the game
    print("Green(Verde)/Yellow(Amarillo) Letters:")
    print("Orange(Naranja) Letters:")
    print("Grey(Gris) Letters:")

    for i in range(6):
        wordss = input(
            "> ")  # might need to remove upper for this part and add it when you get the correct word form autocorrect
        if len(wordss) != 5:
            print("Input word must be 5 letters long.")
            continue
        guess = autocorrect(wordss, palabras).upper()

        if guess.lower() not in words.palabras or len(guess) != 5:
            continue
        else:
            temp_clues = guess, display_wordle(secret, guess)  # calls the functions
            clues.append(temp_clues)
            new_known = known_word(clues)
            print("Known(Conocido) Letters: ", new_known)
            new_yes = yes_letters(clues)
            print("Green(Verde)/Yellow(Amarillo) Letters:", new_yes)
            new_maybe = alternative(clues)
            print("Orange(Naranja) Letters:", new_maybe)
            new_no = no_letters(clues)
            print("Grey(Gris) Letters:", new_no)
            if guess == secret:
                break
            else:
                num_guesses += 1

    print("The secret word was(palabra secreto): ", secret)
    print("Translation:", translation)
