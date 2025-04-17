import subprocess

def run_python_code(code):
    with open("temp.py", "w") as f:
        f.write(code)
    result = subprocess.run(["python", "temp.py"], capture_output=True, text=True)
    return result.stdout or result.stderr
