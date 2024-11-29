import os
import subprocess
import time
import random
import sys
import argparse
from datetime import datetime, timedelta

def message(date):
    """Generate commit message"""
    return f"Contribution: {date.strftime('%Y-%m-%d %H:%M')}"

def run(commands):
    """Execute a command and wait for it to finish"""
    print(f"Running command: {commands}")
    try:
        process = subprocess.Popen(commands, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate(timeout=180)  # Increased timeout to 180 seconds
        if stdout:
            print(stdout.decode())
        if stderr:
            print(stderr.decode())
        process.wait()
    except subprocess.TimeoutExpired:
        print("Timeout expired. The command took too long to execute.")
    except Exception as e:
        print(f"Error executing command: {e}")

def contribute(date):
    """Generate commit and add changes to the repo"""
    print(f"Committing for date: {date}")
    with open(os.path.join(os.getcwd(), 'README.md'), 'a') as file:
        file.write(message(date) + '\n\n')

    print("Running git add...")
    run(['git', 'add', '--all'])  # Use '--all' to add new and modified files

    print("Running git commit...")
    run(['git', 'commit', '-m', message(date), '--date', date.strftime('%Y-%m-%d %H:%M:%S'), '--no-verify', '--quiet', '--allow-empty'])

    print(f"Commit completed for {date}")

def main():
    # Parse arguments
    parser = argparse.ArgumentParser(description="Automate git commits")
    parser.add_argument('--frequency', type=int, default=80, help="Frequency of commits (in seconds)")
    parser.add_argument('--max_commits', type=int, default=17, help="Maximum number of commits")
    parser.add_argument('--repository', type=str, required=True, help="URL of the GitHub repository")
    args = parser.parse_args()

    # Extract repository name from URL (get folder name from the URL)
    repo_name = args.repository.split('/')[-1].replace('.git', '')

    # Clone the repository if it doesn't exist
    if not os.path.exists(repo_name):
        print(f"Cloning repository: {args.repository}")
        run(['git', 'clone', args.repository])

    os.chdir(repo_name)  # Change to the repository directory

    # Start contributing
    current_time = datetime.now()
    commits_made = 0
    while commits_made < args.max_commits:
        contribute(current_time)  # Make a commit for the current time
        commits_made += 1
        print(f"Commit {commits_made}/{args.max_commits} made at {current_time}")

        # Sleep for the desired frequency before making the next commit
        current_time += timedelta(seconds=args.frequency)

        # Random sleep time to simulate natural intervals
        time.sleep(random.uniform(0.5, 1.5))

if __name__ == "__main__":
    main()
