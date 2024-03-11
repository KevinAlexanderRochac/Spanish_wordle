# # word list from: https://www.spanishdict.com/guide/five-letter-spanish-words

import csv
with open ("latin_words.csv", "r") as Latin_files:
    reader = csv.reader(Latin_files)
    words_dict = {rows[0]: rows[1] for rows in reader}

with open ("Latin.txt", "a", encoding ="utf-8") as text_file:
    for key, value in words_dict.items():
        text_file.write("'" + key + "'" + ": " + "'" + value + "'")
        text_file.write("\n")

