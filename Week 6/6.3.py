def first5lines(oldfile, newfile):
    with open(oldfile) as infile, open(newfile, "w") as outfile:
        firstfivelines = infile.readlines()
        num = 1
        for line in firstfivelines:
            strnum = str(num)
            outfile.write(strnum + " " + line)
            num += 1


first5lines("old", "new_ex_6.3")
