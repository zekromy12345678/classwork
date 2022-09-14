# Ask a user their name
name = input("What is your name? ")
# If their first name starts with A or B
if name[0].lower() in ('a', 'b'):
    print("Go to room AB")
# tell them they go to room AB
elif name[0].lower() == 'c' :
    print('Go to room CD')
# IF their first name starts with C
# tell them to go to room CD
else:
    last = input('What is your last name? ')
# If their first name starts with another letter, ask for their last name
if last[0].lower() == 'z':
    print('Go to room Z!')
# IF their last name starts with Z, tell them to go to room Z
else:
    print('go to room OTHER bozo!')
# if their last name starts with any other letter, tell them to go to room OTHER
# When you are done
# Anna should be in room AB
# Bob should be in room AB
# Charlie should be in room C
# Khalid Haque should be in room OTHER
# Xin Zhao should be in room Z