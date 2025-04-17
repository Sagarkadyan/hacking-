import subprocess
import tempfile

def run_code(code):
    with tempfile.NamedTemporaryFile(mode="w+", suffix=".py", delete=False) as temp:
        temp.write(code)
        temp.flush()
        try:
            result = subprocess.run(
                ["python", temp.name],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
            return result.stdout + result.stderr
        except Exception as e:
            return str(e)
