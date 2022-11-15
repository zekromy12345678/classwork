import random as rand
print('Welcome to Coin Toss!!!')
times = int(input('How many times would you like to flip the coin? '))
result = input('\nWoudld you like to see the result of each coin toss? ').lower()
print("\nFlipping!!!\n")
heads = 0
tails = 0
timenum = 0
if result[0] =='y':
  for times in range(0,times):
    timenum = timenum +1
    f1 = rand.choice(["Heads", "Tails"])
    if f1 == 'Heads':
      heads = heads + 1
    else:
      tails = tails +1
    print(f1 + ',')
    if heads == tails:
      print('At '+ str(timenum) + ' flips, the number of heads and tails were equal at'+ str(heads) + ' each.')
    else:
      continue
else:
  for times in range(0,times):
    f1 = rand.choice(["Heads", "Tails"])
    if f1 == 'Heads':
      heads = heads + 1
    else:
      tails = heads +1
perH = (heads/(tails+heads))*100
perT = (tails/(tails+heads))*100
total = times +1
print('Results Of Flipping A Coin ' + str(total) +  ' Times:\n ')
print('Side\tCount\tPercentage')
print('Heads   '+ str(heads)+ '/'+ str(timenum)+'\t'+str(round(perH, 2))+ '%')
print('Tails   '+ str(tails)+ '/'+ str(timenum)+'\t'+str(round(perT, 2))+ '%')