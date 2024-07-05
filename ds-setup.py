import os
import subprocess
import sys

# Define the repositories
repo = {
    "0": "https://github.com/LorenFiorini/0.git",
    "ds": "https://github.com/LorenzoFiorini/data-science-projects.git",
    "archive": "https://github.com/LorenFiorini/_archive.git",
    "gratitude": "https://github.com/LorenFiorini/gratitude.git",
    "journal": "https://github.com/LorenFiorini/journal.git",
    "kaggle": "https://github.com/LorenFiorini/Kaggle.git",
    "42": "https://github.com/LorenFiorini/Python_for_Data_Science.git",
    "market-analysis": "https://github.com/LorenFiorini/Market-Analysis.git"
}

def display_usage():
    '''Display the usage of the script.'''
    print('Usage: python ds-setup.py <repository>')
    print('Available repositories:')
    for key in repo:
        print(f'{key}: {repo[key]}')


def run_git_command(command, cwd):
    """Helper function to run git commands and handle output."""
    try:
        result = subprocess.run(
            command,
            cwd=cwd,
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        # print(f"Command: {' '.join(result.args)}") # Change to nicer formatting
        # TODO: print something like the pwd a '>' or a '$' and the command
        
        print(f"Output: {result.stdout}")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e.stderr}")


def main():
    try:
        # Define the directory and the repository URL from the command line arguments
        if len(sys.argv) == 1:
            raise IndexError
        args = sys.argv[1:]
        for arg in args:
            if arg in repo:
                directory = os.path.expanduser('~') + '/goinfre/' + arg
                repo_url = repo[arg]
                base_dir = os.path.dirname(directory)
                # Check if the directory exists
                if not os.path.exists(directory):
                    print(f'Directory {directory} does not exist. Cloning the repository.')
                    if not os.path.exists(base_dir):
                        os.makedirs(base_dir)
                    run_git_command(['git', 'clone', repo_url, arg], cwd=base_dir)
                else:
                    print(f'Directory {directory} exists. Pulling latest updates from origin.')
                    run_git_command(['git', 'pull', 'origin', 'main'], cwd=directory)
            else:
                print(f'Repository {arg} does not exist.')
    except IndexError:
        print('No repository specified. Exiting.')
        display_usage()
    except Exception as e:
        print(f'Error: {e}')
        display_usage()


if __name__ == "__main__":
    main()
