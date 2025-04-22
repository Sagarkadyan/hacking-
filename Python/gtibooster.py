4'''
keep in ming 
dont judge spelling
this is nit cheating 
do not always follow my code it might delete your whole repo 
soon this project will in its own repo in in a junk repo 
'''
import os
import subprocess
import time
import socket
import random
from datetime import datetime

REPO_PATH = "/home/sagar/Documents/hacking-"
os.chdir(REPO_PATH)

# Wait for internet
''' this function is set to check internet connection if you are unable 
connect in time no process will be continued'''
def wait_for_internet(timeout=60):# this is currently 1 minute change it to convinence
    for i in range(timeout):
        try:
            socket.gethostbyname("github.com")
            return True
        except:
            time.sleep(1)
    return False

if not wait_for_internet():
    print(" Internet not available. Skipping auto commit.")
    exit()

# Remove lock file if it exists
lock_path = os.path.join(REPO_PATH, ".git", "index.lock")
if os.path.exists(lock_path):
    os.remove(lock_path)
    print("Removed old Git lock file.")

# Check for today's commit
log_output = subprocess.getoutput("git log --since=midnight --pretty=oneline")

def make_commits(count, reason="Auto"):
    print(f" Making {count} {reason} commits...")

    for i in range(count):
        with open("autocommit_log.txt", "a") as f:
            f.write(f"{reason} commit {i+1} on {datetime.now().isoformat()}\n")
              

        subprocess.call(["git", "add", "."])
        subprocess.call(["git", "commit", "-m", f"{reason} commit {i+1} "])
        time.sleep(random.randint(2, 5))  # Random delay between commits

    subprocess.call(["git", "push"])
    print(" All commits pushed!")

# Logic
if log_output.strip() == "":
    commit_count = random.randint(1, 4)
    make_commits(commit_count, reason="Initial")
else:
    print("🟢 Already committed today.")
    print("git not updating")
    
    # Random chance to trigger bonus commits
    ''' you can comment this part it is for fun amd extra commit
    ''' 
    bonus_count = random.randint(1, 5)
    print(f"Triggering bonus: making {bonus_count} extra commits!")
    make_commits(bonus_count, reason="Bonus")
