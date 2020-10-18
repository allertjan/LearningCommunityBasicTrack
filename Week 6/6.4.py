def remove_numbers(oldfile, newfile):
    with open(oldfile) as infile, open(newfile, "w") as outfile:
        lines = infile.readlines()
        strnumbers = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0")
        for line in lines:
            if line.startswith(strnumbers):
                newline = " ".join(line.split(" ")[1:])
                outfile.write(newline)
            else:
                outfile.write(line)


remove_numbers("new_ex_6.3", "new_ex_6.4")
