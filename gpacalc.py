#Intro to the calc
print('Welcome to the GPA calculator!\n')
name = input('What your name G? ')
num = int(input("How many grades would you like to enter? "))
#create first list n average
gradelis = [ ]
for x in range(num):
  newgrade = int(input('Please enter grade #' + str(x+1) + '. '))
  x = x+1
  gradelis.append(newgrade)
gradelis.sort(reverse = True)
def Average(gradelis):
    return sum(gradelis) / len(gradelis)
average = Average(gradelis)
print('\nGrades highest to lowest:  ')
#print summary
for x in range(len(gradelis)):
    print('Grade #' + str(x+1) +': ' + str(gradelis[x]))
print('\n'+ f'{name}\'s Grade Summary:')
print('\tTotal number of grades: ' + str(num) + '\n\tHighest Grade: ' + str(gradelis[0]) + '\n\tLowest Grade: ' + str(gradelis[num-1]) + '\n\tAverage: '+ str((round(average, 2))))
#next grade calc
desav = int(input('\nWhat is you desired average? '))
desgrade = (num + 1) * (desav) - sum(gradelis)
print('\nGood luck my boi you need a ' + str(desgrade)+ ' on your next test to get an average of ' + str(desav))
#fake lis and fake average
newlis = gradelis.copy()
chosengrade = int(input('\nWhich grade # would you like to change 1-' + str(num) + ". "))
newchosengrade = int(input('What would you like grade #' + str(chosengrade) + ' to become?' ))
newlis[chosengrade-1] = newchosengrade 
newlis.sort(reverse = True)
def Average2(newlis):
    return sum(newlis) / len(newlis)
average2 = Average2(newlis)
print('\nGrades highest to lowest:  ')
#print summary
for x in range(len(newlis)):
    print('Grade #' + str(x+1) +': ' + str(newlis[x]))
#print fake summary
print('\n'+ f'{name}\'s New Grade Summary:')
print('\tTotal number of grades: ' + str(num) + '\n\tHighest Grade: ' + str(gradelis[0]) + '\n\tLowest Grade: ' + str(newlis[num-1]) + '\n\tAverage: '+ str((round(average2, 2))))
#print comparisons and ending
print('\nYour new average would be a '+ str((round(average2, 2))) + ' compared to your real average of ' + str((round(average, 2))) + '!')
change = average2 - average
print('That is a change of ' + str((round(change, 1))) + ' points!')
print('L bozo your grades are still the same!')
print(gradelis)
print('Better go get some extra credit looser!!!')