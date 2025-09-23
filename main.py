from js import document, window
import random
import asyncio

# Rolling logic
async def roll_dice():
    # Clear previous messages
    for i in range(1, 6):
        div = document.querySelector(f"#rolling{i}")
        div.textContent = ""

    document.querySelector("#roll").textContent = ""

    # Roll values
    result = random.randint(1, 6)
    steps = random.randint(2, 5)

    messages = ["Rolling dice", "Rolling dice.", "Rolling dice..", "Rolling dice...", "Rolling dice"]

    # Animation
    for i in range(steps):
        if i < len(messages):
            document.querySelector(f"#rolling{i+1}").textContent = messages[i]
        await asyncio.sleep(0.5)

    # Show final result
    document.querySelector("#roll").textContent = f"You rolled a {result}"

# Wrapper for event handling
def handle_keydown(event):
    if event.code == "KeyR":
        asyncio.ensure_future(roll_dice())

# Attach event listener
window.addEventListener("keydown", handle_keydown)

# Optional: roll once on page load
# asyncio.ensure_future(roll_dice())
