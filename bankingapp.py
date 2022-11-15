#function that gets base info from user
def getinfo():
    print('Hello welcome to the Banking App!')
    name = input('What is your name? ')
    initialsav = float(input('What would you like your initial savings deposit to be? '))
    initialcheck = float(input('What would you like your initial checking deposit to be? '))
    global info
    info = {
        "Name": name,
        "Savings Amount": initialsav,
        "Checking Amount": initialcheck
    }
#function that asks for edit parameters made to be changeable
def asktypenamount():
    global type
    global amount
    global actionl
    actionl = str(input('Would you like to Withdraw or Deposit? ')).lower()
    type = str(input('Which account, Savings or Checking? ')).lower()
    amount = float(input('How much you wanna ' + str(actionl) + '? '))
#add money to account
def makedeposit(info, type, amount):
    if type == 'savings':
        hello = amount + info.get("Savings Amount")
        info.update({'Savings Amount': hello})
        print('$' + str(amount) + ' depositing...')
        print('\n')
    elif type == 'checking':
        hello = amount + info.get("Checking Amount")
        info.update({'Checking Amount': hello})
        print('$' + str(amount) + ' depositing...')
        print('\n')
#take money from account
def makewithdrawal(info, type, amount):
    if type == 'savings':
        if info.get("Savings Amount") - amount >= 0:
            hello = info.get("Savings Amount") - amount
            info.update({'Savings Amount': hello})
            print('$' + str(amount) + ' withdrawing...')
            print('\n')
        else:
            print('Balance will be negative. Transaction cancelled.')
    elif type == 'checking':
        if info.get("Checking Amount") - amount >= 0:
            hello = info.get("Checking Amount") - amount
            info.update({'Checking Amount': hello})
            print('$' + str(amount) + ' withdrawing...')
            print('\n')
        else:
            print('Balance will be negative. Transaction cancelled.')
#simple display funstion
def displayinfo(info):
    print('Current Account Information: ')
    print('Name: ' + info.get('Name'))
    print('Savings account total: $' + str(info.get('Savings Amount')))
    print('Checking account total: $' + str(info.get('Checking Amount')))
    print()
#main code
getinfo()
print('\n')
i = 0
while i == 0:
    asktypenamount()
    if actionl == 'deposit':
        makedeposit(info, type, amount)
    elif actionl == 'withdraw':
        makewithdrawal(info, type, amount)
    displayinfo(info)
    again = input('Would you like to make another transfer? (y/n) ')
    print()
    if again == 'y':
        continue
    else:
        i += 1
        print('Thank you for using our app!!! Bye Bye.')