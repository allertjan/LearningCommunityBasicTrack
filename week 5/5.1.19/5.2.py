# 5.2

prefixes = "JKLMNOPQ"
suffix = "ack"
prefixes_lower = prefixes.lower()

for letter in prefixes_lower:
    if letter == "q" or letter == "o":
        print(letter + "u" + suffix)
    else:
        print(letter + suffix)
