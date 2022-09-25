#Question 1: Create a class for a vehicle with top speed and mileage instance attributes.
class inventory:
  def __init__(vehicle, make, model, year, topspeed, mileage):
        vehicle.make = make
        vehicle.model = model
        vehicle.year = year
        vehicle.topspeed = topspeed
        vehicle.mileage = mileage
  def info(vehicle):
        print('You have selected a ' + vehicle.year + ' ' + vehicle.make + ' ' + vehicle.model + ' with a top speed of ' + str(vehicle.topspeed) + ' mph and a total of ' + str(vehicle.mileage) + ' miles driven!\n')

model1 = inventory('Ferrari', 'LaFerrari', '2015', 218, 1500)
model2 = inventory('Porche', '918', '2013', 214, 250000)
model3 = inventory('Lamvorgini', 'Aventador SVJ', "2011", 219, 10)
model4 = inventory('Pagani', 'Zonda R', '2008', 230, 0)

option = input('We have 4 models in stock. Which would you like to see? 1-4 ')
if option == "1":
  model1.info()
elif option == "2":
  model2.info()
elif option == "3":
  model3.info()
elif option == "4":
  model4.info()
else:
  print('Please enter either integer 1-4. See you later!')
#Question 2: Create a class for a computer build with specs attributes
class computer:
  def __init__(specs, name, gpu, cpu, ram, fancount):
    specs.name = name
    specs.gpu = gpu
    specs.cpu = cpu
    specs.ram = ram
    specs.fancount = fancount
  def specof(specs):
    print('You have selected a ' + specs.name +' with a ' + specs.gpu + ' and a ' + specs.cpu + 'cpu. The computer also has ' + str(specs.ram) + 'gb of ram and ' + str(specs.fancount) + ' fans!\n')

option = input('We have 3 computer models in stock which would you like to see? 1-3 ')
dell = computer('dell', '1060', 'core i5', 2, 4)
microsoft = computer('microsoft', '2070ti', 'core i5', 32, 20)
macmini = computer('macmini','M1', 'M1', 16, 0)
if option == "1":
  dell.specof()
elif option == "2":
  microsoft.specof()
elif option == "3":
  macmini.specof()
else:
  print('Please enter either integer 1-3. See you later!')

#Question 3: Create a class without any attributes that will move you to the rest of your script
class Derived(computer): 
    pass 
e = Derived("argument changed!", 'gpu', 'cpu', 'ram', 'fancount') 
print (e.name)
#not sure what this does tbh but it has no attributes ???