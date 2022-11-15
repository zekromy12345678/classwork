#create user list
users = ['eramom', 'footea', 'davisv', 'papinukt', 'allenj']
print('Welcome to the Shipping Accounts Program!!!')
#ask username and ask items
username = input('What is your username? ')
if username.lower() in users:
  print('Hello ' + username + '. Welcome back to your account.')
  print('\nCurrent shipping prices are as follows:\n\nShipping orders 0 to 100:    $5.10 each\nShipping orders 100 to 500:  $5.00 each\nShipping orders 500 to 1000: $4.95 each \nShipping orders over 1000:   $4.80 each')
  items = int(input('How many items would you like to ship: '))
  #calculate items
  if items in range(1,101):
    price = 5.10
    cost = items * price
  elif items in range(101,501):
    price = 5.00
    cost = items * price
  elif items in range(501,1001):
    price = 4.95
    cost = items * price
  else:
    price = 4.80
    cost = items * price
  print('To ship'+ str(items) + 'items it will cost you $' + str(round(cost,2)) + 'at $'+ str(price) + ' per item.')
  anotha = input('\nWould you like to place shipment? (y/n) ')
#ask if want to place
  if anotha == 'y' or anotha == 'Y' or anotha == "yes" or anotha == "Yes":
    print('Order placed!!!')
  else:
    print('Okay, no order is being placed at this time.')
else:
  print('Sorry, you do not have an account with us. Goodbye.')