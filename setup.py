import os
import subprocess
import sys

# class Git:
#     def __init__(self, repo_url, directory):
#         self.repo_url = repo_url
#         self.directory = directory

#     def run_git_command(self, command):
#         """Helper function to run git commands and handle output."""
#         try:
#             result = subprocess.run(
#                 command,
#                 cwd=self.directory,
#                 check=True,
#                 stdout=subprocess.PIPE,
#                 stderr=subprocess.PIPE,
#                 text=True
#             )
#             # print(f"Command: {' '.join(result.args)}") # Change to nicer formatting



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
        print(f"cd {cwd} && {' '.join(result.args)}")
        print(f"{result.stdout}")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e.stderr}")


def main():

    try:
        home_directory = os.getenv('HOME')
        url_base = 'https://github.com/LorenFiorini/'
        repo = define_repositories(url_base)
        name = sys.argv[1]
        # Check if the repository is defined
        # repo_url = f'{url_base}{name}.git'
        # if name in repo:
        #     repo_url = repo[name]
        try:
            repo_url = repo[name]
        except KeyError:
            repo_url = f'{url_base}{name}.git'

        # Define the directory
        # dir = f'{home_directory}/goinfre/{name}'
        # if len(sys.argv) > 2:
        #     dir = sys.argv[2] + '/' + name
        try:
            dir = f'{sys.argv[2]}/{name}'
        except IndexError:
            dir = f'{home_directory}/goinfre/{name}'
        base_dir = os.path.dirname(dir)


        # Check if the dir exists
        if not os.path.exists(dir):
            if not os.path.exists(base_dir):
                os.makedirs(base_dir)
            run_git_command(['git', 'clone', repo_url, name], cwd=base_dir)
        else:
            run_git_command(['git', 'pull', 'origin', 'main'], cwd=dir)

    except IndexError:
        print(f'Error: Missing repository argument.')
        display_usage()
    except Exception as e:
        print(f'Error: {e}')




def define_repositories(base_url):
    '''Define the repositories and their URLs.'''
    repo = {
        "ds": "https://github.com/LorenzoFiorini/data-science-projects.git",
        "0": f"{base_url}0.git",
        "archive": f"{base_url}_archive.git",
        "gratitude": f"{base_url}gratitude.git",
        "journal": f"{base_url}journal.git",
        "kaggle": f"{base_url}Kaggle.git",
        "42py": f"{base_url}Python_for_Data_Science.git",
        "market-analysis": f"{base_url}Market-Analysis.git"
    }
    return repo


def display_usage():
    '''Display the usage of the script.'''
    print('Usage: python setup.py <repository>', end='\n\n')
    # print('Available repositories:')
    # for key in repo:
    #     print(f'   {key}')
        # print(f'   {key} \t{repo[key].split("/")[-1].split(".")[0]}')


if __name__ == "__main__":
    main()
