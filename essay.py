name = 'Daniel'
lastname = 'Yadgarov'
school = "SITHS"
sports = ("Swimming", 'handball')
#defined info
stats = {
    'GPA': '4.0',
    'SAT': '1490',
    'APs': '9'
}
#put stats in dict
grades = {
    'chem': 100,
    'math': 98,
    'macro': 95
}
#put grades in dic
totalgrade = str((grades.get('chem') + grades.get('math') + grades.get('macro'))/3)
#took average of grades
colleges = ['Dartmouth', 'Columbia', 'Duke', 'CSI']
#created list of colleges
print('Hello my name is ' + name + ' ' + lastname + '. ' + "I am a student at " + school + '.\n' +
      'Here are some of my academic statistics: ' )
#print out basic info
for key, value in stats.items():
    print(key, ' : ', value)
#pull value from stats dic
print('My current grade average is: ' + totalgrade)
#print tgrade
print('These are the colleges i want to attend: ')
print(*colleges, sep=', ')
#print list seperated by commas