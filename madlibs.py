import random
paragraphs = []
variable_counts = {}

#imports all paragraphs into a list
def importparagraphs():
    with open ('madlibs.txt', 'rt') as file:  # Open lorem.txt for reading
        for x in file:              # For each line, read to a string,
            paragraphs.append(x)    # and print the string.
    return paragraphs
    
#counts the amount of variables in a selected string
def count_variables(chosenpara):
    for word in chosenpara.split():
        if '<' in word and '>' in word:
            index1 = word.index("<") +1
            index2 = word.index(">")
            variable = word[index1:index2]
            if variable in variable_counts:
                variable_counts[variable] += 1
            else:
                variable_counts[variable] = 1
    return variable_counts

#function that gets input
def askvariables(chosenpara):
    for var, count in variable_counts.items():
        response = input(f"Enter a {var}: ")
        chosenpara = chosenpara.replace(f"<{var}>", response)
    return chosenpara

#function that takes input and replaces the variables in the string
"""def replacestrings():
    importparagraphs()
    chosenpara = paragraphs[random.randint(0,len(paragraphs)-1)]
    count_variables(chosenpara)
    print(askvariables(chosenpara))"""

importparagraphs()
chosenpara = paragraphs[random.randint(0,5)]
count_variables(chosenpara)
print(chosenpara)
print(variable_counts)
askvariables(chosenpara)
"""replacestrings()"""
print(chosenpara)