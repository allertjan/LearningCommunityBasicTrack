def count_letters(string):
    counts = {}

    string = string.lower()  # lowercase
    string = "".join(string.split())  # remove whitespace

    for letter in string:
        counts[letter] = counts.get(letter, 0) + 1

    for letter in sorted(counts.keys()):
        print(letter, counts[letter])

    return counts


string = "ThiS is String with Upper and lower case Letters"
count_letters(string)