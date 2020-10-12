def reverse_words(word):
    reversed_word = word[::-1]
    if reversed_word == word:
        return ("It is a palindrome")
    else:
        return ("it is not a palindrome")


print(reverse_words("abb"))

