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
        for line in text:
            for key in dictionary:
                final_line = line.replace(key, dictionary[key])
            outfile.write(final_line)


replace_dictionary("old", "new_ex_6.5", leet_speak)

""""
At line 15 it does change the key into the dictionary[key] however it only remembers it for one specific letter.
When the program goes to the next letter it forgets its previous changes made.
How to solve that?
"""