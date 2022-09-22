#Greet your customer
print('Welcome to Homie City coffee shop!!! \n')
coffeeoptions = {
  "Americano" : 5,
  "Latte" : 2,
  "Black Coffee" : 1,
  "The G special" : 20,
  "Cappuccino" : 4
}
coffeeoptions2 = {
  "americano" : 5,
  "latte" : 2,
  "black coffee" : 1,
  "the g special" : 20,
  "cappuccino" : 4
}
#Ask your customer what their name is with the input() function and store that in the variable NAME.
cusname = input('Yo G was your name? ')
print("\n")
i=0
while i==0:
  print("THIS OUR MENU, GET A LOOK: ")
  for key in coffeeoptions:
    print(key, ':',  '$' + str(coffeeoptions[key]))
  print("\n")
  cusorder = input("Yo " + cusname.upper() + " what would you like from our menu? ")
  cusamount = input('\nBossman ' + cusname + " how many cups u want my guy? ")
  if cusorder.lower() in coffeeoptions2:
      if type(int(cusamount)) == int:
        totalprice = int(coffeeoptions2.get(cusorder.lower())) * int(cusamount)
        print('\nYour total price is $' + str(totalprice) + '\n')
        again = input('Would you like to order more? \n')
        if again.lower() == 'yes':
          print('\n')
        else:
          i = i + 1 
          print("\nHAVE A GREAT DAY HOMIE")
      else:
        i = i +1
        print('\n You did not enter a number. Please Come again later!!!')
  else:
    print('\nThis item is not on our menu. Please come again later!!! ')
    i = i +1
#Greet the customer with their name and thank them for coming in today using concatenation.
#Coffee menu.
#Ask the customer what they would like from the menu and store it in the variable order.
#Ask the customer how many coffees they would like and store it in the variable QUANTITY
#Set the price for coffee
#Calculate the customer's total
#Give the customer their total
#Final statement and asking if they would like anything else.