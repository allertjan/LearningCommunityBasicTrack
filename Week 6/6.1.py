def reverse_files(oldfile, newfile):
    with open(oldfile, "r") as infile, open(newfile, "w") as outfile:
        all_line = infile.readlines()
        all_line.reverse()
        for line in all_line:
            outfile.write(line)


reverse_files("old", "new_ex_6.1")

# Why does this function return the first two list elements without an enter?
