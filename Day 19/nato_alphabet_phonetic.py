import pandas

data = pandas.read_csv("nato_alphabet_phonetic.csv")

phoenetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phoenetic_dict)

def generate_phonetic():
    word = input("Enter a word: ").upper()
    try:
        output_list = [phoenetic_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please")
        generate_phonetic()
    else:
        print(output_list)

generate_phonetic()