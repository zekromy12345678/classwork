# In groups of two to four.
# Go to the Apple or Dell Store online (or a Tech store of your choice) and take inventory of some of the computers they sell.
# Create a Parent class of a computer will all attributes relating to computer specs.
class Inventory:
  def __init__(self,name,price,cpu,gpu,memory,storage,res,size):
    self.name = name
    self.price = price
    self.cpu = cpu
    self.gpu = gpu
    self.memory = memory
    self.storage = storage
    self.res = res
    self.size = size

  def printspecs(self):
    print('\nYou have selected the ' + self.name + "\n\nSpecs:\nCost: $" + str(self.price) + "\nCPU: " + self.cpu 
    + "\nGPU: " + self.gpu + ' \nMemory: ' + self.memory + "\nSTorage: " + self.storage + "\nResolution: " + 
    self.res + "\nSize: " + self.size + '\n')
  
# Create Child classes that will represent all models you will include.
    
pc1= Inventory("Dell XPS 17 Laptop", 2649, "Intel i9-12900HK 14 cores 20 threads","NVIDIA GeForce 3060","32 GB","1 TB","1920 x 1200",'17.0"')
pc2= Inventory("Inspiron 16 Plus Laptop", 2010,"Intel i7-12700H 14 cores 20 threads","NVIDIA GeForce 3060","32 GB","1 TB","3072x1920",'16.0"')
pc3= Inventory("Dell Latitude 9520 Laptop", 2216,"Intel i7-1185G7 4 cores 8 threads","*integrated graphics*","16 GB","1 TB","1920x 1080",'15.0"')
pc4= Inventory("Alienware x17 R2 Laptop", 4550, "Intel i9-12900HK 14 cores 20 threads","NVIDIA GeForce 3080 Ti","64 GB","2 TB","1920x1080",'17.3"')

# Be sure to have user input and program output.
# Also be sure to have iteration taking place in your code
i=0
while i==0:
  option = input('Welcome to Double Daniels computer shop. We have 4 computer models in stock which would you like to see? 1-4 ')
  if option == "1":
    pc1.printspecs()
  elif option == "2":
    pc2.printspecs()
  elif option == "3":
    pc3.printspecs()
  elif option == "4":
    pc4.printspecs()
  else:
    print('Please enter an integer 1-4.')
  anothaone = input('Would you like to see the specs of another model? YES or NO?\n')
  if anothaone.lower() == "yes":
    print('\n')
    continue
  else:
    i = 1
    print('\nThank you for visiting have a great day!')


# Create print functions that will print out models with all specs.

#https://www.dell.com/en-us/shop/dell-laptops/xps-17-laptop/spd/xps-17-9720-laptop/ctox17w11p1c4004
#https://www.dell.com/en-us/shop/dell-laptops/inspiron-16-plus/spd/inspiron-16-7620-laptop/smi16w11p1c205
#https://www.dell.com/en-us/shop/dell-laptops/latitude-9520-laptop-or-2-in-1/spd/latitude-15-9520-2-in-1-laptop/ctol952015us?redirectto=SOC&configurationid=5b91d471-a0f9-4450-b06e-81da07df3bfb#techspecs_section
#https://www.dell.com/en-us/shop/dell-laptops/alienware-x17-r2-gaming-laptop/spd/alienware-x17-r2-laptop/wnr2x17cto41s#tech-specs-anchor