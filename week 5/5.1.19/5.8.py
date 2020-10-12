def mirror_words(sentence):
    reversed_sentence = sentence[::-1]
    mirror_sentence = sentence + reversed_sentence
    return mirror_sentence


print(mirror_words("hello"))
