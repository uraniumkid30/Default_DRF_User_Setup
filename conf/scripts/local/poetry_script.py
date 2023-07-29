import subprocess


def main():
    cmd = ["python", "manage.py", "check"]
    subprocess.run(cmd)
