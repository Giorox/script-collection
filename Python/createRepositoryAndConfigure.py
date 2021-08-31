#!/usr/bin/python
# Script to create a git respository and configure user name and user email using gitPython package
# Usage: python createRepositoryAndConfigure.py
# Author: Giovanni Fazolo Silva Rebouças
# Date: 18 July 2019
# Version: v0.0.1 (18 July 2019)
from git import Repo  # Importing gitPython to operate over repositories
from pathlib import Path  # Import Path composing functions to maintain directory path integrity
import sys  # Import system functionality


def main(argv):
    # Path to where the local repository will be created (if the folder doesn't exist, it will be created)
    source_git_dir = Path(r"C:\Users\USERNAME\test_repository")
    # User's email to show on commits in this repository
    user_email = "example@embraer.com.br"
    # User's name to show on commits in this repository
    user_name = "Embraer Example"

    # Initialize repository at previously defined path
    repo = Repo.init(source_git_dir)
    # Open repository's config writer
    config = repo.config_writer()
    # Set user.email config value
    config.set_value("user", "email", user_email)
    # Set user.name config value
    config.set_value("user", "name", user_name)


if __name__ == "__main__":
    main(sys.argv[1:])
