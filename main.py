import time
import random
from pyscript import document


#Set variables random value
x = random.randint (1,6)
y = random.randint (1,3)
z = random.randint (2,5)

#Prints the value of the variables
output_div = document.querySelector("#output")
if z == 2:
    time.sleep(0.25)
    print ("Rolling dice")
    time.sleep(0.5)
    print ("Rolling dice.")
    time.sleep(0.5)
    print (f"You rolled a {x}")
elif z == 3:
    time.sleep(0.25)
    print ("Rolling dice")
    time.sleep(0.5)
    print ("Rolling dice.")
    time.sleep(0.5)
    print ("Rolling dice..")
    time.sleep(0.5)
    print (f"You rolled a {x}")
elif z == 4:
    time.sleep(0.25)
    print ("Rolling dice")
    time.sleep(0.5)
    print ("Rolling dice.")
    time.sleep(0.5)
    print ("Rolling dice..")
    time.sleep(0.5)
    print ("Rolling dice...")
    time.sleep(0.5)
    print (f"You rolled a {x}")
elif z == 5:
    time.sleep(0.25)
    print ("Rolling dice")
    time.sleep(0.5)
    print ("Rolling dice.")
    time.sleep(0.5)
    print ("Rolling dice..")
    time.sleep(0.5)
    print ("Rolling dice...")
    time.sleep(0.5)
    print ("Rolling dice")
    time.sleep(0.5)
    print (f"You rolled a {x}")