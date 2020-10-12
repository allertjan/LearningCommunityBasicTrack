def replace_words(sentence, old, new):
    new_sentence = sentence.split(old)
    final_sentence = new.join(new_sentence)
    return final_sentence


print(replace_words("hello how are you doing hooi hoih!!", "h", "j"))
