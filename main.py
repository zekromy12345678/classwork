users = ['eramom', 'footea', 'davisv', 'papinukt', 'allenj']
print('Welcome to the Shipping Accounts Program!!!')
username = input('What is your username? ')
if username.lower() in users:
  print('Hello ' + username + '. Welcome back to your account.')
  print('\nCurrent shipping prices are as follows:\n\nShipping orders 0 to 100:    $5.10 each\nShipping orders 100 to 500:  $5.00 each\nShipping orders 500 to 1000: $4.95 each \nShipping orders over 1000:   $4.80 each')
  items = int(input('How many '))
else:
  print('Sorry, you do not have an account with us. Goodbye.')