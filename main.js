async function rollDice() {
    // Clear old messages
    for (let i = 1; i <= 5; i++) {
        document.querySelector(`#rolling${i}`).textContent = "";
    }

    document.querySelector("#roll").textContent = "";

    const messages = [
        "Rolling dice",
        "Rolling dice.",
        "Rolling dice..",
        "Rolling dice...",
        "Rolling dice"
    ];

    // Simulate rolling animation for random steps between 2 and 5
    const steps = Math.floor(Math.random() * 4) + 2; // random int between 2 and 5

    for (let i = 0; i < steps; i++) {
        if (i < messages.length) {
            document.querySelector(`#rolling${i + 1}`).textContent = messages[i];
        }
        await new Promise(resolve => setTimeout(resolve, 500));
    }

    // Show final dice roll result (1-6)
    const result = Math.floor(Math.random() * 6) + 1;
    document.querySelector("#roll").textContent = `You rolled a ${result}`;
}

function onKeydown(event) {
    if (event.code === "KeyR") {
        rollDice();
    }
}

window.addEventListener("keydown", onKeydown);
