import random
paragraphs = []
variable_counts = {}

#imports all paragraphs from text file into a list
def importparagraphs():
    with open ('madlibs.txt', 'rt') as file:  # Open madlibs.txt for reading
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

#function that gets input and replaces the place holders
def askvariablesnreplace(chosenpara):
    c = 0
    for x in variable_counts.keys():
        j = variable_counts[x]
        while c < j:
            response = input(f"Enter a {x}: ")
            chosenpara = chosenpara.replace(f"<{x}>", response , 1)
            c = c+1
        c = 0
    return chosenpara

#main game loop
importparagraphs()
start = input("You have started the Madlibs Ganme! Enter any key to start: ")
z = 0
while z == 0: 
    if len(start) > 0:
        chosenpara = paragraphs[random.randint(0,5)]
        count_variables(chosenpara)
        chosenpara = askvariablesnreplace(chosenpara)
        print("\n" + chosenpara)
        again = input("Would you like to play again? y/n: ")
        if again[0].lower() == "y":
            z = 0
            variable_counts.clear()
            continue
        else:
            print("Thanks for playing!")
            z = 1
    elif len(start) == 0:
        print("Pretty please press a button next time!!!")
        quit()