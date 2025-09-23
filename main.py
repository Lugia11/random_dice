from js import document, console
import random
import asyncio

# Function to roll dice
async def roll_dice():
    # Clear previous text
    for i in range(1, 6):
        document.querySelector(f"#rolling{i}").textContent = ""

    document.querySelector("#roll").textContent = ""

    # Roll logic
    x = random.randint(1, 6)
    z = random.randint(2, 5)

    messages = ["Rolling dice", "Rolling dice.", "Rolling dice..", "Rolling dice...", "Rolling dice"]

    for i in range(z):
        if i < 5:
            document.querySelector(f"#rolling{i+1}").textContent = messages[i]
        await asyncio.sleep(0.5)

    # Show result
    document.querySelector("#roll").textContent = f"You rolled a {x}"

# JavaScript event wrapper
def on_keydown(event):
    if event.code == "KeyR":
        asyncio.ensure_future(roll_dice())

# Add the listener
document.addEventListener("keydown", on_keydown)
