import pandas
# 1. Create a dictionary in this format:
data = pandas.read_csv('nato_phonetic_alphabet.csv')
data_dict = {row.letter: row.code for (index, row) in data.iterrows()}
#2. Create a list of the phonetic code words from a word that the user inputs.
letters = [letter for letter in input('Enter a word: ')]
code = [data_dict.get(letter.upper()) for letter in letters]
print(code)

    

