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
    print('You have selected the ' + self.name + " with a price of $" + str(self.price) + ". This computer runs a " + self.cpu + " cpu and a " + self.gpu + " gpu. It has " + self.memory + "of memory and " + self.storage + "of storage. ")

pc1= Inventory("","","","","","","","")
pc2= Inventory("","","","","","","","")
pc3= Inventory("","","","","","","","")
pc4= Inventory("","","","","","","","")

# Create Child classes that will represent all models you will include.

# Be sure to have user input and program output.
# Also be sure to have iteration taking place in your code

# Create print functions that will print out models with all specs.

#https://www.dell.com/en-us/shop/dell-laptops/xps-17-laptop/spd/xps-17-9720-laptop/ctox17w11p1c4004
https://www.dell.com/en-us/shop/dell-laptops/inspiron-16-plus/spd/inspiron-16-7620-laptop/smi16w11p1c205
https://www.dell.com/en-us/shop/dell-laptops/latitude-9520-laptop-or-2-in-1/spd/latitude-15-9520-2-in-1-laptop/ctol952015us?redirectto=SOC&configurationid=5b91d471-a0f9-4450-b06e-81da07df3bfb#techspecs_section
https://www.dell.com/en-us/shop/dell-laptops/alienware-x17-r2-gaming-laptop/spd/alienware-x17-r2-laptop/wnr2x17cto41s#tech-specs-anchor