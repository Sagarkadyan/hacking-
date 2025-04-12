import os
import subprocess
from datetime import datetime

REPO_PATH = "/home/sagar/Documents/hacking-"

os.chdir(REPO_PATH)

# Check if a commit was made today
log_output = subprocess.getoutput("git log --since=midnight --pretty=oneline")

if log_output.strip() == "":
    # Modify a file or create a dummy log
   
    print("🟢 Already committed today.")
 
else:
    with open("autocommit_log.txt", "a") as f:
        f.write(f"Auto commit on {datetime.now().isoformat()}\n")

    subprocess.call(["git", "add", "."])
    subprocess.call(["git", "commit", "-m", "Auto commit for GitHub activity 💻"])
    subprocess.call(["git", "push"])
    print("✅ Auto commit pushed!")