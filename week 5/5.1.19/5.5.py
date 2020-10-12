import string


def letter_check(text, letter):
    text_without_punc = ""
    for letter in text:
        if letter not in string.punctuation:
            text_without_punc += letter
    text_split = text_without_punc.split()
    total_words = len(text_split)
    words_w_e = 0
    for words in text_split:
        a = words.find(letter)
        if a > 0:
            words_w_e += 1

    return total_words, words_w_e


print(letter_check("hello how are you doing...? I'm very curious about that!", "l"))
