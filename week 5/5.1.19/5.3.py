def count_letters(word, letter):
    count = 0
    for letters in word:
        if letters == letter:
            count += 1
    return count


print(count_letters("hello", "l"))
