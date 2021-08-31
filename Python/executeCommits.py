#!/usr/bin/python
# Script to commit files to a local git repository using gitPython package
# Usage: python executeCommits.py
# Author: Giovanni Fazolo Silva Rebouças
# Date: 18 July 2019
# Version: v0.0.1 (18 July 2019)
from git import Repo  # Importing gitPython to operate over repositories
from pathlib import Path  # Import Path composing functions to maintain directory path integrity
import sys  # Import system functionality
from datetime import datetime  # Import functionality to get current date/time


def main(argv):
    # Path to local repository
    source_git_dir = Path(r"C:\Users\USERNAME\test_repository")
    # Today's date formated as YYYY-MM-DD
    updated_date = datetime.today().strftime('%Y-%m-%d')
    # Commit message
    message = 'Commited on: %s' % (updated_date)

    # Get Repo object from path
    repo = Repo(source_git_dir)
    # Pull INDEX object from Repo object
    index = repo.index
    # Add all files in the "rules" directory to the index (staging area)
    index.add(["rules"])
    # Commit files added to staging area with previously defined message
    index.commit(message)


if __name__ == "__main__":
    main(sys.argv[1:])
