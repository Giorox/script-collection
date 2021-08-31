#!/usr/bin/python
# Script to check if a local repository has more than one branch using gitPython package
# Usage: python checkIfMultipleBranches.py
# Author: Giovanni Fazolo Silva Rebouças
# Date: 18 July 2019
# Version: v0.0.2 (23 August 2019)
# NOTE: Repository should already exist and have a remote named 'origin' configured
from git import Repo  # Importing gitPython to operate over repositories
from pathlib import Path  # Import Path composing functions to maintain directory path integrity
import sys  # Import system functionality


def main(argv):
    # Path to local repository FOLDER
    source_git_dir = Path(r"C:\Users\USERNAME\test_repository")

    repo = Repo(source_git_dir)  # Create Repo object from local folder path
    branches = repo.branches  # Pull repository's branches

    # Check if there is more than 1 branch
    if len(branches) > 1:
        return True
    else:
        return False


# Call main function
if __name__ == "__main__":
    main(sys.argv[1:])
