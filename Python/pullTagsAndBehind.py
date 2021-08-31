#!/usr/bin/python
# Script to pull info from different branches of a local repository using gitPython package
# Usage: python pullTagsAndBehind.py
# Author: Giovanni Fazolo Silva Rebouças
# Date: 18 July 2019
# Version: v0.0.2 (23 August 2019)
# NOTE: Repository should already exist and have a remote named 'origin' configured
from git import Repo  # Importing gitPython to operate over repositories
from pathlib import Path  # Import Path composing functions to maintain directory path integrity
import sys  # Import system functionality
import json  # Import functions to work with JSON files


def main(argv):
    # Path to local repository FOLDER
    source_git_dir = Path(r"C:\Users\USERNAME\test_repository")

    # Create Repo object from the path to the local repository
    repo = Repo(source_git_dir)

    # Assign the remote called "origin" to the o variable
    o = repo.remotes.origin

    # Fetch from the remote called "origin"
    o.fetch()

    # Tags
    tags = []
    # Pull tag info
    for t in repo.tags:
        tags.append({"name": t.name, "commit": str(t.commit), "date": t.commit.committed_date,
                     "committer": t.commit.committer.name, "message": t.commit.message})

    # Get active branch name
    try:
        branch_name = repo.active_branch.name
    except Exception as e:
        print("Something went wrong. Error: " + str(e))
        branch_name = None

    # Get information of commits behind between local master and remote master
    changes = []
    commits_behind = repo.iter_commits('master..origin/master')
    for c in list(commits_behind):
        changes.append({"committer": c.committer.name, "message": c.message})

    # Return JSON files with all information collected previously
    return json.dumps({"tags": tags, "headcommit": str(repo.head.commit), "branchname": branch_name,
                       "master": {"changes": changes}})


if __name__ == "__main__":
    main(sys.argv[1:])
