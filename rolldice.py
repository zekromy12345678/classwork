import random as rand
def dice_sides():
    sides = int(input("\nHow many sides would you like on your dice? "))
    return sides
def dice_number():
    number = int(input("How many dice would you like to roll? "))
    return number
def roll_dice(sides, number):
    dice = []
    print("\nYou rolled a " + str(sides) + " sided dice  " + str(number) + " times.")
    print("\n-----Results are as followed-----")
    for i in range(number):
        value = rand.randint(1, sides)
        print("\t" + str(value))
        dice.append(value)
    return dice
def sum_dice(dice):
    print("\nThe total value of all your rolls is " + str(sum(dice)) + ".")
def roll_again():
    choice = input("\nWould you like to roll again (y/n): ").lower().strip()
    if choice[0] == "y":
        roll = 0
    else:
        roll = 1
    return roll
def goodbye(roll):
  if roll == 0:
    pass
  else:
    print('Goodbye!')
roll = 0
print('Welcome to the Python Dice App')
while roll<1:
  dsides = dice_sides()
  dnumber = dice_number()
  ddice = roll_dice(dsides, dnumber)
  sum_dice(ddice)
  roll = roll_again()
  goodbye(roll)