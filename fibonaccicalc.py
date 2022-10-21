print('Welcome to the Fibonacci Calculator')
num = int(input("\nHow many digits would you like to compute?\n"))
print('\n')
lis = [1, 1]
print(0)
#calculates fibonacci sequence
for x in range(num-1):
  print(lis[x])
  hello = lis[x] + lis[x+1]
  lis.append(hello)
#compute the golden ratio
print('\n')
print('undefined')
for i in range(num-1):
  hello = lis[i] + lis[i+1]
  ratio = lis[i+1]/lis[i]
  print(ratio)
  lis.append(hello)
#tells the user the golden ratio
print('\nthe golden ratio is 1.618033988749894...')