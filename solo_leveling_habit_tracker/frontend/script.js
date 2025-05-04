const username = 'jinwoo';
let level = 1;
let xp = 0;
const xpPerLevel = 100;

async function loadStats() {
    const res = await fetch(`http://127.0.0.1:5000/get_stats?username=${username}`);
    if (res.ok) {
        const data = await res.json();
        level = data.level;
        xp = data.xp;
        updateUI();
    }
}

async function saveStats() {
    await fetch("http://127.0.0.1:5000/update_stats", {
        method: "POST",
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ username, level, xp })
    });
}

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

document.addEventListener("DOMContentLoaded", async () => {
    await loadStats();
    document.getElementById("pushupBtn").addEventListener("click", () => {
        addXP(25);
    });
});