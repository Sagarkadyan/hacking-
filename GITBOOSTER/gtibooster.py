import os
import subprocess
import time
import socket
from datetime import datetime

REPO_PATH = "/home/sagar/Documents/hacking-"
os.chdir(REPO_PATH)

# Wait for internet
def wait_for_internet(timeout=1000):
    for i in range(timeout):
        try:
            socket.gethostbyname("github.com")
            return True
        except:
            time.sleep(1)
    return False

if not wait_for_internet():
    print("❌ Internet not available. Skipping auto commit.")
    exit()

# Check for existing lock file and delete
lock_path = os.path.join(REPO_PATH, ".git", "index.lock")
if os.path.exists(lock_path):
    os.remove(lock_path)
    print("🔓 Removed old Git lock file.")

# Check if commit exists today
log_output = subprocess.getoutput("git log --since=midnight --pretty=oneline")

if log_output.strip() == "":
    with open("autocommit_log.txt", "a") as f:
        f.write(f"Auto commit on {datetime.now().isoformat()}\n")

    subprocess.call(["git", "add", "."])
    subprocess.call(["git", "commit", "-m", "Auto commit for GitHub activity 🚀"])
    subprocess.call(["git", "push"])
    print("✅ Auto commit pushed!")
else:
    #print("🟢 Already committed today.")
      with open("autocommit_log.txt", "a") as f:
        f.write(f"Auto commit on {datetime.now().isoformat()}\n")

     subprocess.call(["git", "add", "."])
     subprocess.call(["git", "commit", "-m", "Auto commit for GitHub activity 🚀"])
     subprocess.call(["git", "push"])
     print("✅ Auto commit pushed!")
