# 5.2

prefixes = "JKLMNOPQ"
suffix = "ack"
prefixes_lower = prefixes.lower()

for letter in prefixes_lower:
    if letter == "q":
        print(letter + "u" + suffix)
    elif letter == "o":
        print(letter + "u" + suffix) # Waarom werkt een or statement niet voor de letters q en o?
    else:
        print(letter + suffix)
