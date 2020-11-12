leet_speak = {
    "l": "1",
    "e": "3",
    "a": "4",
    "o": "0",
    "r": "7",
}

def replace_dictionary(oldfile, newfile, dictionary):
    with open(oldfile) as infile, open(newfile, "w") as outfile:
        text = infile.readlines()
        final_line = ""
        for line in text:
            for letter in line:
                if letter in leet_speak:
                    for key in dictionary:
                        final_letter = letter.replace(key, dictionary[key])
                        final_line += final_letter
                else:
                    final_line += letter
                outfile.write(final_line)


replace_dictionary("old", "new_ex_6.5", leet_speak)

""""
At line 15 it does change the key into the dictionary[key] however it only remembers it for one specific letter.
When the program goes to the next letter it forgets its previous changes made.
How to solve that?
"""