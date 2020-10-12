'''
a. >>> dictionary = {"apples": 15, "bananas": 35, "grapes": 12}
>>> dictionary["bananas"] # print 35
b. >>> dictionary["oranges"] = 20  # change 35 to 20
>>> len(dictionary) # give length of dictionary
c. >>> "grapes" in dictionary # checks if grapes is in dictionary
d. >>> dictionary["pears"] # returns error because pearse is not in dictionary
e. >>> dictionary.get("pears", 0) # error
f. >>> fruits = list(dictionary.keys())
>>> fruits.sort()
>>> print(fruits) # will make a list of dictionary and arrange it to fruits and then it will be sorted on alphabetic order
g. >>> del dictionary["apples"] # delete apples
>>> "apples" in dictionary # false
'''