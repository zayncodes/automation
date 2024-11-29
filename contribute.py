import random
import os
import subprocess

# Function to run a command
def run_command(command):
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    return result.stdout, result.stderr

# Randomize the number of commits (between 1 and 17)
num_commits = random.randint(1, 17)

# List of random commit messages
messages = ['Message 1', 'Message 2', 'Message 3', 'Message 4', 'Message 5', 'Message 6', 
            'Message 7', 'Message 8', 'Message 9', 'Message 10', 'Message 11', 'Message 12',
            'Message 13', 'Message 14', 'Message 15', 'Message 16', 'Message 17']

# Stage and commit a random number of changes
def commit_changes():
    for i in range(num_commits):
        commit_message = random.choice(messages)
        run_command(['git', 'add', '.'])
        run_command(['git', 'commit', '-m', commit_message])

# Push changes to the remote repository
def push_changes():
    run_command(['git', 'push', 'origin', 'main'])

# Main function to execute the tasks
def main():
    # 80% chance to run the script (0.8 probability)
    if random.random() < 0.8:
        print("Proceeding with commits and push...")
        os.chdir('C:/Users/niles/Desktop/automation')
  # Change to your script's directory
        commit_changes()
        push_changes()
    else:
        print("No commits today. Try again tomorrow.")

if __name__ == '__main__':
    main()
