#!/usr/bin/python
# Script to commit and push to a remote repository using gitPython package
# Usage: python commitAndPushToRemote.py
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
    # Commit message
    message = 'Commited through gitPython'

    try:
        # Create Repo object from specified path
        repo = Repo(source_git_dir)
        # Add all changed files to staging area
        repo.git.add(update=True)
        # Commit changes with choosen message
        repo.index.commit(message)
        # Pull ref that points to the remote called 'origin'
        origin = repo.remote(name='origin')
        # Push to remote (origin)
        origin.push()
    except Exception as e:
        print("Something went wrong while pushing the code. Error: " + str(e))
    finally:
        print("Code push from gitPython succeeded")


if __name__ == "__main__":
    main(sys.argv[1:])
