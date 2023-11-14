import os
import subprocess

# Get project path
project_path = os.getcwd()

# Initialize a Git repository
subprocess.run(['git', 'init', '-b', 'main'], cwd=project_path)

# Check if pre-commit is installed
try:
    import pre_commit
except ModuleNotFoundError:
    print("pre-commit is not installed. Installing it now...")
    subprocess.run(['pip', 'install', 'pre-commit'], cwd=project_path)

# Run pre-commit install in your Git repository
subprocess.run(['pre-commit', 'install'], cwd=project_path)