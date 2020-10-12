def remove_substrings(word, substring):
    new_word = word.replace(substring, "")
    return new_word


print(remove_substrings("mississippi", "iss"))