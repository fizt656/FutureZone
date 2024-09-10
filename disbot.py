import subprocess
import sys
import os

def run_bot():
    if len(sys.argv) < 2:
        print("Usage: python disbot.py <character_name>")
        sys.exit(1)

    character_name = sys.argv[1]

    while True:
        process = subprocess.Popen([sys.executable, 'main.py', character_name])
        process.wait()
        
        if process.returncode == 0:
            print("Bot stopped deliberately. Exiting...")
            break
        elif process.returncode == 1:
            print("Bot restarting...")
        else:
            print("Bot crashed or exited unexpectedly. Restarting...")

if __name__ == "__main__":
    run_bot()