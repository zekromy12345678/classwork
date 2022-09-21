# A for loop is used for iterating over a sequence (list, tuple, dictionary, or set)
studenthitlist = ['Jessica', 'Daniel', 'Daniella', 'Cynthia', 'Fruci']
for x in studenthitlist:
  print(x)
print ('\n')
# Using a for loop to loop through a string
for string in 'HELLLLLLLLLO':
  print(string)
print('\n')
# Using the break statement to stop a loop before it has looped through all the items
endname = input('Which name is the worst? Jessica, Daniel, Daniella, Cynthia, or Fruci ')
print('\n')
studenthitlist = ['jessica', 'daniel', 'daniella', 'cynthia', 'fruci']
for x in studenthitlist:
  if x != endname.lower():
    print(x)
  else:
    break
print('\n')
# Using the continue statement to stop the current iteration, and loop to the next
skipnum = int(input('What number do you want to skip? '))
print('\n')
num = 0
while num < 9:
  num += 1
  if num == skipnum:
    continue
  print(num)
print('\n')
# To loop through a set of code a specified number of times, we can use range() function
runloop = int(input("How many computers do you want to hack? "))
print('\n')
i = 0
while i in range(0,runloop):
  i = i+1
  print("YOU HACKED " + str(i) + (' COMPUTERS!!!!! GGEZ'))