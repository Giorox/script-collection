#!/usr/bin/python
# Script to pull and print information from local repository using gitPython package
# Usage: python pullRepositoryInfo.py
# Author: Giovanni Fazolo Silva Rebouças
# Date: 18 July 2019
# Version: v0.0.2 (23 August 2019)
# NOTE: Repository should already exist and have a remote named 'origin' configured
from git import Repo  # Importing gitPython to operate over repositories
from pathlib import Path  # Import Path composing functions to maintain directory path integrity


# How many commits to print (starting from the latest commit)
COMMITS_TO_PRINT = 5


# Print commit hash, summary, author name, author email, date and time of commit, number of files and overall commit size
def print_commit(commit):
    print('----')
    print(str(commit.hexsha))
    print("\"{}\" by {} ({})".format(commit.summary,
                                     commit.author.name,
                                     commit.author.email))
    print(str(commit.authored_datetime))
    print(str("count: {} and size: {}".format(commit.count(),
                                              commit.size)))


# Print repository description, what is the active branch, print the repository's remotes and respective urls and print the latest commit
def print_repository(repo):
    print('Repo description: {}'.format(repo.description))
    print('Repo active branch is {}'.format(repo.active_branch))
    for remote in repo.remotes:
        print('Remote named "{}" with URL "{}"'.format(remote, remote.url))
    print('Last commit for repo is {}.'.format(str(repo.head.commit.hexsha)))


if __name__ == "__main__":
    # Create Path object to local repository
    repo_path = Path(r"C:\Users\USERNAME\test_repository")
    # Repo object used to programmatically interact with Git repositories
    repo = Repo(repo_path)
    # Check that the repository loaded correctly and is not a bare repository
    if not repo.bare:
        print('Repo at {} successfully loaded.'.format(repo_path))
        # Print some repository details
        print_repository(repo)
        # create list of commits
        commits = list(repo.iter_commits('master'))[:COMMITS_TO_PRINT]
        # Print commits and commit info to stdout
        for commit in commits:
            print_commit(commit)
            pass
    else:
        print('Could not load repository at {} :('.format(repo_path))
