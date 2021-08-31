#!/usr/bin/python
# Script to fetch a remote repository to a local git repository using gitPython package
# Usage: python fetchFromRemote.py
# Author: Giovanni Fazolo Silva Rebouças
# Date: 18 July 2019
# Version: v0.0.1 (18 July 2019)
from git import Repo  # Importing gitPython to operate over repositories
from pathlib import Path  # Import Path composing functions to maintain directory path integrity
import sys  # Import system functionality
import os  # Import directory and other OS functionality
import shutil  # Import functions to work with directory trees efficiently


def main(argv):
    # Path to local repository FOLDER (make sure it's not pointing to somewhere you don't want to lose anything)
    source_git_dir = Path(r"C:\Users\USERNAME\test_repository")
    # URL to remote repository
    remote_url = "https://git.embraer.com.br/scm/dmu/support.git"

    # Check if the directory exists, if it does, delete it entirely
    if os.path.isdir(source_git_dir):
        shutil.rmtree(source_git_dir)

    # Create directory at specified path
    os.mkdir(source_git_dir)

    # Initialize repository at newly created folder
    repo = Repo.init(source_git_dir)
    # Create ref towards remote called 'origin'
    origin = repo.create_remote('origin', remote_url)
    # Fetch from newly created remote
    origin.fetch()
    # Pull files from HEAD
    origin.pull(origin.refs[0].remote_head)


if __name__ == "__main__":
    main(sys.argv[1:])
