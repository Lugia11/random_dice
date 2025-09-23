from js import document
import random
import asyncio

# Async dice roll function
async def roll_dice():
    x = random.randint(1, 6)
    z = random.randint(2, 5)

    messages = [
        "Rolling dice",
        "Rolling dice.",
        "Rolling dice..",
        "Rolling dice...",
        "Rolling dice"
    ]

    # Clear previous roll text
    for i in range(1, 6):
        div = document.querySelector(f"#rolling{i}")
        div.textContent = ""

    result_div = document.querySelector("#roll")
    result_div.textContent = ""

    # Animate "Rolling dice..." messages
    for i in range(z):
        if i < len(messages):
            div = document.querySelector(f"#rolling{i+1}")
            div.textContent = messages[i]
            await asyncio.sleep(0.5)

    # Final result
    result_div.textContent = f"You rolled a {x}"

# Async event listener for keydown
async def on_keydown(event):
    if event.code == "KeyR":
        await roll_dice()

# Register the keydown event listener
document.addEventListener("keydown", on_keydown)
