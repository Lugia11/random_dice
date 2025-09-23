from js import document
import random
import asyncio

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

    # Loop through the number of rolling messages based on z
    for i in range(z - 1):
        div = document.querySelector(f"#rolling{i+1}")
        div.textContent = messages[i]
        await asyncio.sleep(0.5)

    # Final result
    result_div = document.querySelector("#roll")
    result_div.textContent = f"You rolled a {x}"

# Call the function when script loads
asyncio.ensure_future(roll_dice())
