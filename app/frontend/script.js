const username = 'jinwoo'; // static for now — can be dynamic with login

let level = 1;
let xp = 0;
const xpPerLevel = 100;

// Get user data from backend
async function loadStats() {
    const res = await fetch(`http://127.0.0.1:5000/get_stats?username=${username}`);
    if (res.ok) {
        const data = await res.json();
        level = data.level;
        xp = data.xp;
        updateUI();
    }
}

// Save user data to backend
async function saveStats() {
    await fetch("http://127.0.0.1:5000/update_stats", {
        method: "POST",
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ username, level, xp })
    });
}

// UI logic
function updateUI() {
    document.getElementById('level').textContent = level;
    document.getElementById('xp').textContent = `${xp}/${xpPerLevel}`;
    document.getElementById('xpBar').style.width = `${(xp / xpPerLevel) * 100}%`;
}

function addXP(amount) {
    xp += amount;
    if (xp >= xpPerLevel) {
        xp -= xpPerLevel;
        level++;
    }
    updateUI();
    saveStats();
}

// Triggered on page load
document.addEventListener("DOMContentLoaded", async () => {
    await loadStats();

    document.getElementById("pushupBtn").addEventListener("click", () => {
        addXP(25);
    });
});
