from js import document, window
import random
import asyncio

async def roll_dice():
    # Clear old messages
    for i in range(1, 6):
        document.querySelector(f"#rolling{i}").textContent = ""

    document.querySelector("#roll").textContent = ""

    messages = [
        "Rolling dice", 
        "Rolling dice.", 
        "Rolling dice..", 
        "Rolling dice...", 
        "Rolling dice"
    ]

    # Simulate rolling animation for random steps between 2 and 5
    steps = random.randint(2, 5)

    for i in range(steps):
        if i < len(messages):
            document.querySelector(f"#rolling{i+1}").textContent = messages[i]
        await asyncio.sleep(0.5)

    # Show final dice roll result (1-6)
    result = random.randint(1, 6)
    document.querySelector("#roll").textContent = f"You rolled a {result}"

def on_keydown(event):
    if event.code == "KeyR":
        asyncio.ensure_future(roll_dice())

window.addEventListener("keydown", on_keydown)
