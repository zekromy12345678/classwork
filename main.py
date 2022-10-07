filled = {"u1": 0, 'u2': 0, "u3": 0, "m1": 0, "m2": 0, "m3": 0, "l1": 0, "l2": 0, "l3": 0,}
class tictac:
  def __init__(space, u1, u2, u3, m1, m2, m3, l1, l2, l3):
    space.u1 = u1
    space.u2 = u2
    space.u3 = u3
    space.m1 = m1
    space.m2 = m2
    space.m3 = m3
    space.l1 = l1
    space.l2 = l2
    space.l3 = l3
# define a print board
  def printboard(space):
    print('\n' + space.u1 + '|' + space.u2 + '|' + space.u3 + '\n______\n' + space.m1+ '|' + space.m2 + '|' + space.m3 + '\n______\n' + space.l1 + '|' + space.l2 + '|' +space.l3 + '\n')
# define a player move
  def askuser1(space):
    placement = input("player 1 where would you like to place x? u1, u2, u3, m1, m2, m3, l1, l2 , l3. ")
    if filled[placement] == 0:
      if placement == 'u1':
        space.u1 = 'x'
        filled["u1"] += 1
      elif placement == 'u2':
        space.u2 = 'x'
        filled["u2"] += 1
      elif placement == 'u3':
        space.u3 = 'x'
        filled["u3"] += 1
      elif placement == 'm1':
        space.m1 = 'x'
        filled["m1"] += 1
      elif placement == 'm2':
        space.m2 = 'x'
        filled["m2"] += 1
      elif placement == 'm3':
        space.m3 = 'x'
        filled["m3"] += 1
      elif placement == 'l1':
        space.l1 = 'x'
        filled["l1"] += 1
      elif placement == 'l2':
        space.l2 = 'x'
        filled["l2"] += 1
      elif placement == 'l3':
        space.l3 = 'x'
        filled["l3"] += 1
    else:
      print('wrong')
      
  def askuser2(space):
    placement = input("player 2 where would you like to place you o? u1, u2, u3, m1, m2, m3, l1, l2 , l3. ")
    if filled[placement] == 0:
      if placement == 'u1':
        space.u1 = 'o'
        filled["u1"] += 1
      elif placement == 'u2':
        space.u2 = 'o'
        filled["u2"] += 1
      elif placement == 'u3':
        space.u3 = 'o'
        filled["u3"] += 1
      elif placement == 'm1':
        space.m1 = 'o'
        filled["m1"] += 1
      elif placement == 'm2':
        space.m2 = 'o'
        filled["m2"] += 1
      elif placement == 'm3':
        space.m3 = 'o'
        filled["m3"] += 1
      elif placement == 'l1':
        space.l1 = 'o'
        filled["l1"] += 1
      elif placement == 'l2':
        space.l2 = 'o'
        filled["l2"] += 1
      elif placement == 'l3':
        space.l3 = 'o'
        filled["l3"] += 1
    else:
      print('wrong')
# define what is victory
  def checkvic(space, i):
    if space.u1 + space.u2 + space.u3 == 'xxx' or space.u1 + space.u2 + space.u3 == 'ooo':
      i = i +1 
      print('Victory!')
    elif space.m1 + space.m2 + space.m3 == 'xxx' or space.m1 + space.m2 + space.m3 == 'ooo':
      i = i +1 
      print('Victory!')
    elif space.l1 + space.l2 + space.l3 == 'xxx' or space.l1 + space.l2 + space.l3 == 'ooo':
      i = i +1 
      print('Victory!')
    elif space.u1 + space.m1 + space.l1 == 'xxx' or space.u1 + space.m1 + space.l1 == 'ooo':
      i = i +1
      print('Victory!')
    elif space.u2 + space.m2 + space.l2 == 'xxx' or space.u2 + space.m2 + space.l2 == 'ooo':
      i = i +1 
      print('Victory!')
    elif space.u3 + space.m3 + space.l3 == 'xxx' or space.u3 + space.m3 + space.l3 == 'ooo':
      i = i +1 
      print('Victory!')
    elif space.u1 + space.m2 + space.l3 == 'xxx' or space.u1 + space.m2 + space.l3 == 'ooo':
      i = i +1 
      print('Victory!')
    elif space.u3 + space.m2 + space.l1 == 'xxx' or space.u3 + space.m2 + space.l1 == 'ooo':
      i = i +1 
      print('Victory!')
    else:
      pass
    return i
# define what a draw is
  def checkdraw(space ,i):
    if filled["u1"] + filled["u2"] + filled["u3"] + filled["m1"] + filled["m2"] +filled["m3"] + filled["l1"] + filled["l2"] + filled["l3"] == 9:
      i = i + 1
      print('IT''s a draw!')
    else:
      pass
    return i
# Create a Loop for iteration

pos = tictac(' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ')
i=0
while i == 0:
  tictac.printboard(pos)
  tictac.askuser1(pos)
  i = tictac.checkvic(pos, i)
  i = tictac.checkdraw(pos, i)
  if i==0:
    tictac.printboard(pos)
    tictac.askuser2(pos)
    i = tictac.checkvic(pos, i)
    i = tictac.checkdraw(pos, i)
    if i == 1:
      print('Game over! Thanks for playing!!')
      keeplay = input('Would you like to play again? y/n')
      if keeplay == 'y':
        pos = tictac(' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ')
        filled = {"u1": 0, 'u2': 0, "u3": 0, "m1": 0, "m2": 0, "m3": 0, "l1": 0, "l2": 0, "l3": 0,}
        i = 0
    else:
      continue
  elif i == 1:
    print('Game over! Thanks for playing!!')
    keeplay = input('Would you like to play again? y/n')
    if keeplay == 'y':
      pos = tictac(' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ')
      filled = {"u1": 0, 'u2': 0, "u3": 0, "m1": 0, "m2": 0, "m3": 0, "l1": 0, "l2": 0, "l3": 0,}
      i=0
    else:
      continue