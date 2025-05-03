let xp = 40;
function gainXP() {
  xp += 10;
  if (xp > 100) xp = 100;
  document.getElementById("xpFill").style.width = xp + "%";
  document.getElementById("xpValue").innerText = xp;
}
