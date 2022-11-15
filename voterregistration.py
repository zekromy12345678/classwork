print('Welcome to Voter registration app!')
name = input('What is your name? ').title().strip()
age = int(input('What is your age? '))
parties = ['Republican', 'Democratic', 'Independent', 'Libertarian', 'Green']
if age > 17:
  print('\nCongratulations '+ name + '! You are old enough to register to vote.')
  print('\nHere is a list of political parties to join:')
  [print('\t- '+ i) for i in parties]
  party = input('What party would you like to register as? ').title().strip()
  if party in parties:
    if party == 'Republican' or party == 'Democratic':
      print('Congrats! You have been registered and joined a major party!')
    elif party == 'Independent':
      print('Congrats! You have been registered as an Independent!')
    else:
      print('Congrats! You have been registered and not joined a major party!')
  else:
    print('Your party is not in the list. This is not a true democracy. Please retry!')
else:
  comeback = 18 - age
  print('Your a youngster. Please come back in ' + str(comeback) + ' year(s)!')