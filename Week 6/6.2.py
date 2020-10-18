def snake_printer(oldfilename, newfilename):
    with open(oldfilename) as infile, open(newfilename, "w") as outfile:
        for line in infile:
            if "snake" in line:
                outfile.write(line)


snake_printer("old", "new_ex_6.2")
