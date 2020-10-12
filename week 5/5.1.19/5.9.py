def remove_letter(word, letter):
    final_word = ""
    for x in word:
        if x != letter:
            final_word += x
    return final_word


print(remove_letter("hello", "e"))
