"""
Module: farming_diary
This script simulates a farming diary where different crops (corn and rice) are grown, watered,
and checked for ripeness.
"""

from farm.corn import Corn
from farm.rice import Rice


print("\n\n📝 Day One: Corn")

# 1. Instantiate a corn crop
my_corn = Corn()
    
# 2. Water the corn crop
my_corn.water()
   

# 3. Print "The corn crop produced ## grains"
print(f"The corn crop produced {my_corn.grains} grains")

# 4. Print "The corn crop is ripe" or "The corn crop is not ripe"
if my_corn.ripe():
    print("The corn crop is ripe")
else: 
    print("The corn crop is not ripe")

print("\n\n📝 Day Two: Rice")

# 1. Instantiate a rice crop
my_rice = Rice()

# 2. Water the rice crop
my_rice.water()

# 3. Transplant the rice crop
my_rice.water()


# 4. Print "The rice crop produced ## grains"
print(f"The rice crop produced {my_rice.grains} grains")

# 5. Print "The rice crop is ripe" or "The rice crop is not ripe"
if my_rice.ripe():
    print("The rice crop is ripe")
else:
    print("The rice crop is not ripe")


my_rice2 = Rice()
my_rice2.water()
my_rice2.transplant()
my_rice2.transplant()
my_rice2.transplant()

if my_rice2.ripe():
    print(f"The rice2 crop is ripe {my_rice2.grains}")
else:
    print("The rice crop is not ripe")

