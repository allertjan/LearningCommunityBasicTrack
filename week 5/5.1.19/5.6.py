n = int(input('Please enter a positive integer between 1 and 15: '))

for row in range(1, n+1):
    for col in range(1, n+1):
        print(row*col, end="\t")
    print()

''' 
could not solve the question so searched on the internet. 
link: https://stackoverflow.com/questions/20415384/properly-formatted-multiplication-table
'''