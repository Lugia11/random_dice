from js import document
import time
import random

# Set variables random value
x = random.randint(1, 6)
y = random.randint(1, 3)
z = random.randint(2, 5)

# Prints the value of the variables
if z == 2:
    time.sleep(0.25)
    output_div = document.querySelector("#rolling")
    output_div.textContent = "Rolling dice"
    time.sleep(0.5)
    output_div = document.querySelector("#rolling")
    output_div.textContent = "Rolling dice."
    time.sleep(0.5)
    output_div = document.querySelector("#roll")
    output_div.textContent = f"You rolled a {x}"
elif z == 3:
    time.sleep(0.25)
    output_div = document.querySelector("#rolling")
    output_div.textContent = "Rolling dice"
    time.sleep(0.5)
    output_div = document.querySelector("#rolling")
    output_div.textContent = "Rolling dice."
    time.sleep(0.5)
    output_div = document.querySelector("#rolling")
    output_div.textContent = "Rolling dice.."
    time.sleep(0.5)
    output_div = document.querySelector("#roll")
    output_div.textContent = f"You rolled a {x}"
elif z == 4:
    time.sleep(0.25)
    output_div = document.querySelector("#rolling")
    output_div.textContent = "Rolling dice"
    time.sleep(0.5)
    output_div = document.querySelector("#rolling")
    output_div.textContent = "Rolling dice."
    time.sleep(0.5)
    output_div = document.querySelector("#rolling")
    output_div.textContent = "Rolling dice.."
    time.sleep(0.5)
    output_div = document.querySelector("#rolling")
    output_div.textContent = "Rolling dice..."
    time.sleep(0.5)
    output_div = document.querySelector("#roll")
    output_div.textContent = f"You rolled a {x}"
elif z == 5:
    time.sleep(0.25)
    output_div = document.querySelector("#rolling")
    output_div.textContent = "Rolling dice"
    time.sleep(0.5)
    output_div = document.querySelector("#rolling")
    output_div.textContent = "Rolling dice."
    time.sleep(0.5)
    output_div = document.querySelector("#rolling")
    output_div.textContent = "Rolling dice.."
    time.sleep(0.5)
    output_div = document.querySelector("#rolling")
    output_div.textContent = "Rolling dice..."
    time.sleep(0.5)
    output_div = document.querySelector("#rolling")
    output_div.textContent = "Rolling dice"
    time.sleep(0.5)
    output_div = document.querySelector("#roll")
    output_div.textContent = f"You rolled a {x}"
